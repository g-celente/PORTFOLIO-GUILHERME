import requests
from database import Connection
from datetime import datetime
import time

class Moeda:
    def __init__(self):
        self.url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL'

    def get_url(self):
        response = requests.get(self.url)
        self.response_json = response.json()

    def get_coin(self):
        cotacao_dolar = self.response_json['USDBRL']['bid']
        cotacao_euro = self.response_json['EURBRL']['bid']
        date = datetime.now()
        date2 = datetime.now()
        result = [
            ['Dolar', cotacao_dolar, date, date2], 
            ['Euro', cotacao_euro, date, date2], 
        ]

        db = Connection()
        db.create_database()
        for i in result:
            name = i[0]
            cotacao = i[1]
            data = i[2]
            data2 = i[3]
            db.insert_coin(name, cotacao, data, data2)
        db.close_database()

        print(f'Cotação Atualizada: {date}')

def start_data_collection():
    while True:
        cotacao = Moeda()
        cotacao.get_url()
        cotacao.get_coin()
        time.sleep(3600)

if __name__ == "__main__":
    start_data_collection()