import threading
import socket


def send_all(message):
    for client in clients:
        client.send(message)


def send(message, client):
    client.send(message.encode('utf-8'))


def help(client):
    while True:
        msg = client.recv(1024)
        if msg.decode('utf-8').endswith('#choose'):
            client.send(f'{nicknames}'.encode('utf-8'))
            user = client.recv(1024)
            full_nick = user.decode('utf-8')
            nick = full_nick.split(' ')
            print(nick)
            client.send("Ваше сообщение:\n".encode('utf-8'))
            msg = client.recv(1024)
            full_msg = msg.decode('utf-8')
            print(full_msg)
            whisper(full_msg, nick[1])
        elif msg.decode('utf-8').endswith("q"):
            client.send(f'До свидания!'.encode('utf-8'))
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            send_all(f'{nickname} покинул(-a) чат.'.encode('utf-8'))
            nicknames.remove(nickname)
            break
        else:
            send_all(msg)


def client_recieve():
    while True:
        client, address = server.accept()
        client.send('username'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print(nicknames)
        send_all(f'{nickname} подключился к чату!'.encode('utf-8'))
        client.send(
            '\nДля отправки личного сообщения используйте команду "#choose"\nДля выхода из чата отправьте "q"'.encode(
                'utf-8'))
        thread = threading.Thread(target=help, args=(client,))
        thread.start()


def whisper(message, name):
    if name in nicknames:
        name_index = nicknames.index(name)
        client_to_whisper = clients[name_index]
        send(message, client_to_whisper)


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 2045))
    server.listen()
    clients = []
    nicknames = []
    print('Запуск сервера...')
    client_recieve()
