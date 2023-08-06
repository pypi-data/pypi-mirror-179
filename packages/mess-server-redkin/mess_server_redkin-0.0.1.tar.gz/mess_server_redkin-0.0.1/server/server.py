"""Программа-сервер. Разработал Редкин И.А. декабрь 2022 г."""

import binascii
import dis
import hmac
import os
import sys
import threading
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import logging
import select
import logs.config_server_log
from common.variables import DEFAULT_PORT, MAX_CONNECTIONS, ACTION, TIME, \
    USER, ACCOUNT_NAME, FROM, PRESENCE, ERROR, MESSAGE, \
    MESSAGE_TEXT, RESPONSE_400, TO, RESPONSE_200, EXIT, GET_ALL_CLIENTS, RESPONSE_202, ALERT, GET_MY_CONTACTS, \
    ADD_CONTACT, CONTACT_NAME, AUTH, STATE, REG, PASSWORD_HASH, PUBLIC_KEY, RESPONSE_511, DATA, RESPONSE
from common.utils import get_msg, send_msg, log

from server_db import ServerStorage

SERVER_LOGGER = logging.getLogger('server')


class ServerVerifier(type):
    """Метакласс. Проверка на корректность класса сервера.
    Необходимо использовать сокеты для работы по TCP протоколу.
    """

    def __new__(cls, future_class_name, future_class_parents, future_class_attrs):

        lst_argval = []
        for func in future_class_attrs:
            try:
                ret = dis.get_instructions(future_class_attrs[func])
            except TypeError:
                pass
            else:
                for i in ret:
                    lst_argval.append(i.argval)
        if 'connect' in lst_argval:
            raise 'Вызов connect должен отсутствовать для сокетов сервера'
        if 'AF_INET' not in lst_argval or 'SOCK_STREAM' not in lst_argval:
            raise 'Необходимо использовать сокеты для работы по TCP протоколу'

        return type.__new__(cls, future_class_name, future_class_parents, future_class_attrs)


class PortDescriptor:
    """Класс-дескриптор. Корректность установки номера порта."""
    def __init__(self, default=DEFAULT_PORT):
        self.default = default

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.my_attr, self.default)

    def __set__(self, instance, value):
        if value < 1024 or value > 65535:
            raise ValueError
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


@log
def arg_parser():
    """Разбор аргументов командной строки.
    -a - адрес;
    -p - порт;
    """
    listen_port = 7777
    listen_address = ''
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
    except IndexError:
        SERVER_LOGGER.error("При запуске клиента после параметра '-p' не указан номер порта.")
        exit()
    except ValueError:
        SERVER_LOGGER.error('При запуске клиента неверно указан номер порта.')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''
    except IndexError:
        SERVER_LOGGER.error("При запуске клиента после параметра '-a' не указан адрес.")
        sys.exit(1)

    return listen_port, listen_address


class Server(metaclass=ServerVerifier):
    """Основной класс. Обменивается информацией с клиентами."""
    port = PortDescriptor()

    def __init__(self, listen_port, listen_address, database):
        super().__init__()
        self.db = database
        self.port = listen_port
        self.address = listen_address
        self.clients = []
        self.messages = []
        self.all_users = []
        self.names = dict()

    @log
    def process_client_message(self, message, messages_list, client, clients, names):
        """Разбирает словарь-сообщение от клиента."""
        SERVER_LOGGER.debug(f'Разбор сообщения от клиента : {message}')
        if ACTION in message and message[ACTION] == PRESENCE and \
                TIME in message and USER in message:
            # Если пользователь авторизуется
            if message[USER][STATE] == AUTH:
                if self.db.check_user(message[USER][ACCOUNT_NAME]):
                    # Процесс авторизации
                    SERVER_LOGGER.debug('Correct username, starting passwd check.')
                    message_auth = RESPONSE_511
                    random_str = binascii.hexlify(os.urandom(64))
                    message_auth[DATA] = random_str.decode('ascii')
                    hash = hmac.new(self.db.get_hash(message[USER][ACCOUNT_NAME]), random_str, 'MD5')
                    digest = hash.digest()
                    SERVER_LOGGER.debug(f'Auth message = {message_auth}')
                    try:
                        send_msg(client, message_auth)
                        ans = get_msg(client)
                    except OSError as err:
                        SERVER_LOGGER.debug('Error in auth, data:', exc_info=err)
                        client.close()
                    client_digest = binascii.a2b_base64(ans[DATA])
                    if RESPONSE in ans and ans[RESPONSE] == 511 and hmac.compare_digest(
                            digest, client_digest):
                        self.names[message[USER][ACCOUNT_NAME]] = client
                        return
                else:
                    self.response = RESPONSE_400
                    self.response[ERROR] = f'Пользователь {message[USER][ACCOUNT_NAME]} не зарегистрирован'
                    send_msg(client, self.response)
                    clients.remove(client)
                    client.close()
                return
            elif message[USER][STATE] == REG:
                if self.db.check_user(message[USER][ACCOUNT_NAME]):
                    self.response = RESPONSE_400
                    self.response[ERROR] = f'Имя {message[USER][ACCOUNT_NAME]} уже занято.'
                    send_msg(client, self.response)
                    clients.remove(client)
                    client.close()
                else:
                    self.db.add_user(message[USER][ACCOUNT_NAME],
                                     message[USER][PASSWORD_HASH],
                                     message[USER][PUBLIC_KEY])
                    clients.remove(client)
                    client.close()

        elif ACTION in message and message[ACTION] == MESSAGE and \
                TO in message and TIME in message \
                and FROM in message and MESSAGE_TEXT in message:
            self.db.insert_in_contactdb(message[FROM], message[TO], message[MESSAGE_TEXT], message[TIME])
            messages_list.append(message)
            return
        elif ACTION in message and message[ACTION] == GET_ALL_CLIENTS and ACCOUNT_NAME in message:
            self.response = RESPONSE_202
            for user in self.db.get_all_users():
                self.all_users.append(user.login)
            self.response[ALERT] = self.all_users
            send_msg(client, self.response)
            return
        elif ACTION in message and message[ACTION] == EXIT and ACCOUNT_NAME in message:
            clients.remove(names[message[ACCOUNT_NAME]])
            names[message[ACCOUNT_NAME]].close()
            del names[message[ACCOUNT_NAME]]
            return
        else:
            self.response = RESPONSE_400
            self.response[ERROR] = 'Запрос некорректен.'
            send_msg(client, self.response)
            return

    @log
    def process_message(self, message, names, listen_socks):
        """Отправляет сообщение от одного пользователя другому."""
        if message[TO] in names and names[message[TO]] in listen_socks:
            send_msg(names[message[TO]], message)
            SERVER_LOGGER.info(f'Отправлено сообщение пользователю {message[TO]} '
                               f'от пользователя {message[FROM]}.')
        elif message[TO] in names and names[message[TO]] not in listen_socks:
            raise ConnectionError
        else:
            SERVER_LOGGER.error(
                f'Пользователь {message[TO]} не зарегистрирован на сервере, '
                f'отправка сообщения невозможна.')

    def main(self):
        """Запуск сервера. Установка соединений с клиентами.
        Получение сообщений от клиентов. Отправка сообщения клиентам."""
        SERVER_LOGGER.info(
            f'Запущен сервер, порт для подключений: {self.port}, '
            f'адрес с которого принимаются подключения: {self.address}. '
            f'Если адрес не указан, принимаются соединения с любых адресов.')
        sock = socket(AF_INET, SOCK_STREAM)
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind((self.address, self.port))
        sock.settimeout(0.5)

        self.sock = sock
        self.sock.listen()

        while True:
            try:
                client, addr = self.sock.accept()
            except OSError:
                pass
            else:
                SERVER_LOGGER.info(f'Установлено соедение с ПК {addr}')
                self.clients.append(client)

            self.r_clients = []
            self.w_clients = []

            try:
                if self.clients:
                    self.r_clients, self.w_clients, _ = select.select(self.clients, self.clients, [], 0)
            except OSError:
                pass

            if self.r_clients:
                for client_with_message in self.r_clients:
                    try:
                        self.process_client_message(get_msg(client_with_message),
                                                    self.messages, client_with_message, self.clients, self.names)
                    except Exception:
                        SERVER_LOGGER.info(f'Клиент {client_with_message.getpeername()} '
                                           f'отключился от сервера.')
                        self.clients.remove(client_with_message)

            # Если есть сообщения, обрабатываем каждое.
            for msg in self.messages:
                try:
                    self.process_message(msg, self.names, self.w_clients)
                    print('Сообщение отправлено')
                except Exception:
                    SERVER_LOGGER.info(f'Связь с клиентом с именем {msg[TO]} была потеряна')
                    self.clients.remove(self.names[msg[TO]])
                    del self.names[msg[FROM]]
            self.messages.clear()


if __name__ == '__main__':
    listen_port, listen_address = arg_parser()
    database = ServerStorage()

    s = Server(listen_port, listen_address, database)
    s.main()
