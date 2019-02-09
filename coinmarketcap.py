import requests
data={}
r=0
#A dictionary is created with the keys (characters) and values (names) of all cryptocurrencies that are on the CoinMarketCap website
#Создается словарь с ключами(символами) и значениями(именами) всех криптовалют , которые есть на сайте CoinMarketCap
while True:
        result=requests.get(f'https://api.coinmarketcap.com/v1/ticker/?start={r}').json()
        i=0
        if 'error' in result:
                break
        while i!=len(result):
                data[result[i]['symbol'].lower()]=data.get(result[i]['symbol'].lower(),result[i]['id'])
                i+=1
        r+=100
#Function to get the current price of cryptocurrency
#Функция для получения актуальной цены криптовалюты
def get_coin(Id):
        resp=requests.get(f'https://api.coinmarketcap.com/v1/ticker/{Id}/').json()
        return (f"{resp[0]['price_usd']}$ , +{resp[0]['percent_change_24h']}% " if float(resp[0]['percent_change_24h'])>0 else f"{resp[0]['price_usd']}$ , {resp[0]['percent_change_24h']}% ")
