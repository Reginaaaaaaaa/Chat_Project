## Задачи:

1) Написать консольный чат
	  * Несколько пользователей могут общаться друг с другом
	  * Для выбора собеседника сервер отправляет список действующих клиентов
		
2) Оформить код и представить его

## Какие модули использовались?

Основными используемыми модулями были: Socket и Threading

### Краткий экскурс в модули Socket и Threading
        
Сокет — это программный интерфейс для обеспечения информационного обмена между процессами. С его помощью мы можем подключать клиентов к серверу по определнному порту и адресу.

Модуль Threading значительно упрощает работу с потоками и позволяет программировать запуск нескольких операций одновременно.

Благодаря перовму модулю мы реализовываем подключение клиентов к серверу и обмен между ними информации, а благодаря второму реализовываем отправку и принятие сообщений.

## Наглядная работа кода:

Запуск сервера и подключение пользователей.
Пользователи видят оповещения о новых подключениях и общаются друг с другом.

<a href="https://ibb.co/g4Zp0Wx"><img src="https://i.ibb.co/Z2zPQg0/Screenshot-from-2022-05-31-09-08-11.png" alt="Screenshot-from-2022-05-31-09-08-11" border="0"></a>

Отправка личных сообщений.
Пользователь сначала выбирает получателя, а после пишет сообщение, которое хочет ему отправить.

<a href="https://ibb.co/F3TD86r"><img src="https://i.ibb.co/bm9KN10/Screenshot-from-2022-05-31-09-08-50.png" alt="Screenshot-from-2022-05-31-09-08-50" border="0"></a>

Выход из чата.
Все пользователи получают оповещение об отключении этого пользователя.

<a href="https://ibb.co/CBr12FG"><img src="https://i.ibb.co/MnX26L0/Screenshot-from-2022-05-31-09-08-59.png" alt="Screenshot-from-2022-05-31-09-08-59" border="0"></a>

## Принцип работы (со стороны сервера)

Импортируем модули.

```
import threading
import socket
```
Данная функция отвечает за отправление сообщений всем пользователям.

```
def send_all()
```
Отправка сообщений также вынесена в отдельную функцию.

```
def send()
```
Функция, которая обрабатывает, сообщения.
Здесь происходит поиск команд на отправку личного сообщения или выхода.
Если команд не было найдено, то сообщение отправляется всем.

```
def help()
```
Авторизация пользователя. Уведомление всех в чате о новом подключении и добавление клиента в списки.

```
def client_recieve()
```

Для отправки личного сообщения.

```
def ls()
```

## Принцип работы (со стороны клиента)

Импортируем модули.

```
import socket
import threading
```

Эта функция постоянно приниает сообщения.
Ответное сообщение отправляется только если пришло сообщение для авторизации от сервера.

```
def server_recieve()
```

Функция отправки сообщений.

```
def send()
```
