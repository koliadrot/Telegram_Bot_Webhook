from flask import Flask
from flask import request
from flask import jsonify
from flask_sslify import SSLify

from data_api_bot import *
from coinmarketcap import *

import requests
import json
import datetime


app=Flask(__name__)
sslify=SSLify(app)

#Class with the main functions of the bot
#Класс с основными функциями бота
class BotHandler:
        def __init__(self, token):
                self.token = token
                self.api_url = f"https://api.telegram.org/bot{token}/"
        def send_message(self, chat_id, text):
                params = {'chat_id': chat_id, 'text': text}
                resp = requests.post(self.api_url + 'sendMessage', params)
        def delete_message(self,chat_id,message_id):
                params = {'chat_id':chat_id,'message_id': message_id}
                resp = requests.post(self.api_url + 'deleteMessage', params)
                
bot = BotHandler(token)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        now = datetime.datetime.now()
        r = request.get_json()
        last_chat_id=r['message']['chat']['id']
        last_message_id=r['message']['message_id']
        last_chat_name=r['message']['from']['first_name']
        try:
            last_chat_text=r['message']['text']
        except KeyError:
            pass
        #Welcome bot depending on the time of day with a time shift
        #Приветствие бота в зависимости от времени суток со сдвигом по времени
        if last_chat_text.lower()[0]=="/" and last_chat_text.lower()[1::] in greetings and 6 <= now.hour+2 < 12:
            bot.send_message(last_chat_id, f'Доброе утро, {last_chat_name}!')
        elif last_chat_text.lower()[0]=="/" and last_chat_text.lower()[1::] in greetings and 12 <= now.hour+2 < 17:
            bot.send_message(last_chat_id, f'Добрый день, {last_chat_name}!')
        elif last_chat_text.lower()[0]=="/" and last_chat_text.lower()[1::] in greetings and 17 <= now.hour+2 < 23:
            bot.send_message(last_chat_id, f'Добрый вечер, {last_chat_name}!')
        elif last_chat_text.lower()[0]=="/" and last_chat_text.lower()[1::] in greetings and ((now.hour+2)>=23 or (now.hour+2)<6):
            bot.send_message(last_chat_id, f'Доброго времени суток, {last_chat_name}!')
        #The bot uses the public api of CoinMarketCap to get the current price of cryptocurrency
        #Бот использует  публичный api CoinMarketCap,для получения актуальной цены криптовалюты
        elif last_chat_text.lower()[1::] in data.keys() and last_chat_text.lower()[0]=="/":
            bot.send_message(last_chat_id,get_coin(data[last_chat_text.lower()[1::]]))
        #Sends message info (see module data_api_bot). Be sure to put your bot name in '/info@<your bot name`s>'
        #Отправляет сообщение info(см.модуль data_api_bot).Обязательно нужно поставить имя вашего бота в '/info@<your bot name`s>'
        elif last_chat_text.lower()== '/info@<your bot name`s>' or last_chat_text.lower()== '/info':
            bot.send_message(last_chat_id,info)
        #The bot deletes obscene language messages found in bad_words (see module data_api_bot)
        #Бот удаляет сообщения с нецензурной лексикой найденные в bad_words(см.модуль data_api_bot)
        if bad_words & {last_chat_text.lower()}:
            bot.delete_message(last_chat_id,last_message_id)
            bot.send_message(last_chat_id,prejudice)
    return "<h1>Welcome!</h1>"


if __name__=="__main__":
    app.run()