import socket
import threading

username = input("Введите ваш ник:\n")  # пользователь вводит свой ник

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 2045))  # подключение к серверу


def server_recieve():  # функция, принимающая сообщения
    while True:
        message = client.recv(1024).decode('utf-8')
        if message == 'username':  # сообщение от сервера для авторизации пользователя
            client.send(username.encode('utf-8'))
        else:
            print(message)  # если сообщение не от сервера, то просто выводим его


def send():  # функция для отправки сообщений
    while True:
        message = f'{username}: {input()}'  # ввод пользователем сообщения и его отправка
        client.send(message.encode('utf-8'))


# запускаем отправку и прием сообщений в потоках
recieve_thread = threading.Thread(target=server_recieve)
recieve_thread.daemon = True
recieve_thread.start()
send_thread = threading.Thread(target=send)
send_thread.start()
