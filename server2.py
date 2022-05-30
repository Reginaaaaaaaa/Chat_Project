import threading
import socket


def send_all(message):  # Функция, которая будет отсылать сообщение всем подключенным клиентам
    for client in clients:
        client.send(message)


def send(message, client):  # Функция, которая отправляет сообщения
    client.send(message.encode('utf-8'))


def help(client):  # Здесь обрабатываются клиентские сообщения
    while True:
        msg = client.recv(1024)
        if msg.decode('utf-8').endswith('#choose'):
            # Смотрим на наличие специальной команды в пришедшем сообщении
            # Если команда присутствует, то клиент хочет отправить личное сообщение
            client.send(f'{nicknames}'.encode('utf-8'))  # отправляем список пользователей для выбора получателя
            user = client.recv(1024)
            # далее обрабатываем полученное сообщение-это должен быть ник получателя
            full_nick = user.decode('utf-8')
            nick = full_nick.split(' ')
            # делим по пробелу, чтобы получить имя получателя
            print(nick)  # вывод на сервере для достоверности
            client.send("Ваше сообщение:\n".encode('utf-8'))
            # теперь уже отправитель печатает сообщение, которое он хочет отправить лично
            msg = client.recv(1024)  # получаем это сообщение
            full_msg = msg.decode('utf-8')
            print(full_msg)  # вывод на сервере для достоверности
            ls(full_msg, nick[1])  # отправляем нужному пользователю
        elif msg.decode('utf-8').endswith("q"):
            # Команда для выхода из чата и оповещения всех об отключении клиента
            client.send(f'До свидания!'.encode('utf-8'))
            # не забываем попрощаться с пользователем, вежливость-это важно!
            index = clients.index(client)  # соотносим сокет и его индекс, чтобы удалить его из списка
            clients.remove(client)
            client.close()
            nickname = nicknames[index]  # для удаления ника из списка, который мы отправляем всем
            send_all(f'{nickname} покинул(-a) чат.'.encode('utf-8'))  # оповещаем всех об уходе пользователя
            nicknames.remove(nickname)
            break
        else:
            send_all(msg)  # если никакой команды не поступило, то просто отправляем сообщение всем клиентам


def client_recieve():
    while True:
        client, address = server.accept()  # Подключение пользователей, получение их сокета и адреса
        client.send('username'.encode('utf-8'))  # отправляем сообщение пользователю дл получение его ника и авторизации
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)  # заносим его пользователя в массивы
        clients.append(client)
        print(nicknames)  # каждый раз при подключении пользователя на сервере мы будем видеть это в массиве
        send_all(f'{nickname} подключился к чату!'.encode('utf-8'))
        # также оповещаем всех пользователей о новом подключении
        client.send(
            '\nДля отправки личного сообщения используйте команду "#choose"\nДля выхода из чата отправьте "q"'.encode(
                'utf-8'))  # приветственное сообщение со списком команд
        thread = threading.Thread(target=help, args=(client,))  # функция обработки работает в отдельном потоке
        thread.start()


def ls(message, name):  # функция для отправки личного сообщения
    if name in nicknames:  # ищем нужного клиента
        name_index = nicknames.index(name)
        client_to_whisper = clients[name_index]  # соотносим индексы для отправки сообщения
        send(message, client_to_whisper)  # передаем в функцию для отправки само сообщение и получателя


if __name__ == '__main__':  # исполнение основной программы
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # запуск сервера
    server.bind(('localhost', 2045))
    server.listen()
    clients = []
    nicknames = []
    print('Сервер запущен...')
    client_recieve()  # функция авторизации пользователя

