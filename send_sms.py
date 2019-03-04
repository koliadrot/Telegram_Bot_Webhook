import requests
#Логин аккаунта
#Account login
accountSid="Your_accountSid"
#Ваш api токен
#Your API token
authToken="Your_token"
#Список разрешенных номеров,на которые можно отправлять смс (Только в пробной версии)
#The list of allowed numbers to which you can send SMS (Only in trial version)
list_verify_numbers=[]

def send_sms(to_number,text):
    data={
    "From":"Your_sender_number",
    "To":to_number,
    "Body":text,
    }
    auth=(accountSid,authToken)
    res=requests.post(f"https://api.twilio.com/2010-04-01/Accounts/{accountSid}/Messages",data=data,auth=auth)
