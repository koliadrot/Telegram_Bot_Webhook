import sendgrid
import os
from sendgrid.helpers.mail import *
from data_api_bot import *
#The function that sends a message to email through the service Sendgrid
#Функция, отправляющая сообщение на email через сервис Sendgrid
def send_email(email,subject,text):
    sg = sendgrid.SendGridAPIClient(apikey=token_sg)
    from_email = Email("your_email_name`s")
    to_email = Email(email)
    content = Content("text/plain",text)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
