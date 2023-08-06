import sys
from PyQt6.QtWidgets import QApplication
from client.window_dialog import WindowDialog
from client.client_DB import ClientStorage
from common.variables import *
from common.errors import ServerError
from client.transport import ClientTransport
from client.main_window import ClientMainWindow
from logs.client_log_config import log

# Инициализация клиентского логера
logger = log

# Основная функция клиента
if __name__ == '__main__':

    # Обработка параметров коммандной строки
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        client_name = sys.argv[3]
        if 1024 > server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
        client_name = None
    except ValueError:
        logger.error('Номер порт должен находиться в диапазоне  [1024 - 65535]')
        print('Номер порт должен находиться в диапазоне  [1024 - 65535]')
        sys.exit(1)

    # Создаём клиентское приложение
    client_app = QApplication(sys.argv)

    # Если имя пользователя не было указано в командной строке, то запросим его
    if not client_name:
        app = QApplication(sys.argv)
        window = WindowDialog()
        window.show()
        app.exec()
        if window.ok_pressed:
            client_name = window.client_name.text()
            client_passwd = window.client_passwd.text()
    # Записываем логи
    logger.info(
        f'Запущен клиент с параметрами: адрес сервера: {server_address} , порт: {server_port},'
        f'имя пользователя: {client_name}')

    # Создаём объект базы данных
    database_client = ClientStorage(client_name)
    database_client.init()

    # Создаём объект - транспорт и запускаем транспортный поток
    try:
        transport = ClientTransport(server_port, server_address, database_client, client_name, client_passwd)
    except ServerError as error:
        transport = None
        print(error.text)
        exit(1)
    transport.setDaemon(True)
    transport.start()

    # Создаём GUI
    main_window = ClientMainWindow(database_client, transport, client_name)
    main_window.make_connection(transport)
    main_window.clients_list_update()
    main_window.setWindowTitle(f'Чат Программа alpha release - {client_name}')
    client_app.exec()

    # Раз графическая оболочка закрылась, закрываем транспорт
    transport.transport_shutdown()
    transport.join()
    