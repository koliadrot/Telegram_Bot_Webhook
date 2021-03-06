EN:

Telegram Bot with Webhook

The main task of this bot, to respond to user requests, about the current price of a certain cryptocurrency.
Also, there are additional functions for convenient operation via the Telegram messenger, such as: send
messages and SMS to the mailbox directly through the chat channel telegram.

This bot works as follows: The bot accepts the request from the Server Telegrams and the bot processing 
the data sends the data to the server.

This method is effective compared to the reverse method of Webhook (the bot itself requests(spam) telegrams 
server,and the telegram server responds to it), since the delay between the bot and the server almost 
disappears and the unsatisfactory results that could pass between requests disappear.

Useful notes to get started:
1. Don't forget to insert your Telegram token in the data_api_bot file - the variable "token"

2. For correct operation of the function of sending messages, you need to register on
   Sendgrid website (https://sendgrid.com/pricing/), choose the free version by following
   instructions on the site to get your Sendgrid token, when you need to insert it in the file
   data_api_bot - the variable "token_sg" and write the name of the sender in the send_email file
   variable "from_email". Do not forget when creating a token on the Sendgrid website, give
   your token has all the authority when working with a message so that there are no problems with the rights.
3. To work correctly, the function of sending SMS to phone numbers, you need to go to
   Twilio website (https://www.twilio.com/) and register. On the main page, you will need
   get accountSid and authToken, where you will need to insert them in the send_sms file - variables
   "accountSid" and "authToken". The next step is to create a number from which
   send SMS, for this you need to go to the Phone Number-Manage Numbers tab and select
   Active Numbers. After receiving your number, you need to copy and paste it into the file
   send_sms - variable "From". In the trial version, you can call and send SMS only to
   pre-checked numbers (In the full version, you can call and send SMS without checking).
   To add a number to the list of checked numbers, go to the tab Phone Number -
   Manage Numbers and select Verified Caller IDs (You can add as many numbers as you like).
   After checked the numbers, click in the file send_sms - in the list "list_verify_numbers"
   (This is only required for the trial version of the account! In the full version it is not required!)
   Send media files only to the numbers of residents of the United States and Canada! Cost of one
   messages = $ 0.045. In the trial version, $ 15 is automatically credited to the account.

4. The bot was placed on the site of the service - https://www.pythonanywhere.com
   The cost of the service is free, you only need to renew it every 3 months, this too
   is free!

Details on the methods Telegram bot look at - https://core.telegram.org/bots/api

RU: 

Телеграмм Бот с Webhook 

Главная задача этого бота, отвечать на запросы пользователей, об актуальной цене определенной криптовалюты. 
Так же, есть дополнительные функции для удобной работы через мессенджер Телеграм, такие как:отправлять 
сообщения на почтовый ящик и на мобильные номера непосредственно через сам чат телеграм-канала. 

Данный бот работает по следующему принципу: Бот принимает запрос от Телеграмм сервера и бот обрабатывая дан- 
ные, отправляет данные серверу. 

Данный метод эффективен по сравнению с методом обратному Webhook(Бот сам запрашивает(спамит) телеграмм сервер, 
а телеграмм сервер ему отвечает), так как задержка между ботом и сервером практически исчезает и пропадают не- 
удовлетворительные результаты, которые могли проходить между запросами. 

Полезные заметки для начала работы: 
1. Не забудьте вставить ваш токен Телеграмма в файле data_api_bot - переменная "token"

2. Для исправной работы функции отправления сообщений почтовый ящик, нужно перейти на
   сайт Sendgrid(https://sendgrid.com/pricing/) и зарегистрироваться, выбрать бесплатную
   версию, следуя инструкциям на сайте получить ваш токен Sendgrid,где надо будет вставить
   в файле data_api_bot - переменная "token_sg" и написать имя отправителя в файле send_email
   переменная "from_email". Не забудьте при создании токена на сайте Sendgrid, дать
   вашему токену все уполномочия при работе с сообщения, чтобы небыло проблем с правами.

3. Для исправной работы функции отправления смс на телефонные номера, нужно перейти на
   сайт Twilio(https://www.twilio.com/) и зарегистрироваться.На главной странице, нужно будет
   получить accountSid и authToken,где надо будет вставить их в файле send_sms - переменные 
   "accountSid" и "authToken".Следующим шагом, нужно создать номер, с которого будут
   отправляться смс, для этого нужно перейти в вкладку Phone Number-Manage Numbers и выбрать 
   Active Numbers.После получения вашего номера, его нужно скопировать и вставить в файле
   send_sms - переменная "From".В пробной версии, можно звонить и отправлять смс только на 
   заранее проверенные номера(В полной версии можно звонить и отправлять смс без проверки).
   Чтобы добавить номер в лист проверенных номеров, перейти в вкладку Phone Number -
   Manage Numbers и выбрать Verified Caller IDs (Добавлять можно сколько угодно номеров).
   После проверенные номера нажно вставить в файле send_sms - в список "list_verify_numbers"
   (Это требуется только для пробной версии аккаунта! В полной версии это не требуется!)
   Отправлять медиа файлы, можно только на номера резидентов США и Канады! Стоимость одного
   сообщения = 0,045$.В пробной версии на счет автоматически зачисляется 15$.

4. Сам бот размещался на сайте сервиса - https://www.pythonanywhere.com
   Стоимость услуги бесплатная, нужно только каждые 3 месяца продливать, это тоже бесплатно!

Подробно о методах Телеграмм бота смотреть на - https://core.telegram.org/bots/api
Подробно о процессе получения необходимых данных Twilio читать на - https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account

