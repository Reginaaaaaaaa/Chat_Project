import socket
import threading


username = input("Введите ваш ник:\n")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 2045))


def server_recieve():
    while True:
        message = client.recv(1024).decode('utf-8')
        if message == 'username':
            client.send(username.encode('utf-8'))
        else:
            print(message)


def send():
    while True:
        message = f'{username}: {input()}'
        client.send(message.encode('utf-8'))


recieve_thread = threading.Thread(target=server_recieve)
recieve_thread.daemon = True
recieve_thread.start()
write_thread = threading.Thread(target=send)
write_thread.start()
