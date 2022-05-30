# Задачи:

1) Написать консольный чат
	  * Несколько пользователей могут общаться друг с другом
	  * Для выбора собеседника сервер отправляет список действующих клиентов
		
2) Оформить код и представить его

# Какие модули использовались?

Основными используемыми модулями были: Socket и Threading

        <b>Краткий экскурс в модули Socket и Threading<b>
        
Сокет — это программный интерфейс для обеспечения информационного обмена между процессами. С его помощью мы можем подключать клиентов к серверу по определнному порту и адресу.

Модуль Threading значительно упрощает работу с потоками и позволяет программировать запуск нескольких операций одновременно.

Благодаря перовму модулю мы реализовываем подключение клиентов к серверу и обмен между ними информации, а блягодаря второму реализовываем отправку и принятие сообщений.