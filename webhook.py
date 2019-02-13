import requests
from data_api_bot import token,proxies
#The function to "hook" your url address to the servers Telegram
#Функция , чтобы "зацепить" ваш url адрес к серверам Телеграмма
def set_Webhook(url):
    params={"url":url}
    r=requests.post(f"https://api.telegram.org/bot{token}/"+"setWebhook",params,proxies=proxies)
    return r.json()
#The function to remove your "hook"
#Функция ,чтобы удалить ваш hook
def delete_Webhook():
    r=requests.post(f"https://api.telegram.org/bot{token}/"+"deleteWebhook",proxies=proxies)
    return r.json()
#The to get relevant about your webhook"
#Функция , чтобы получить актуальную о вашем Webhook 
def get_Webhook_info():
    r=requests.get(f"https://api.telegram.org/bot{token}/"+"getWebhookinfo",proxies=proxies)
    return r.json()

if __name__=="__main__":
    print(get_Webhook_info())
