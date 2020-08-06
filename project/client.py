import requests
from random import choice, uniform, randrange
from uuid import uuid4
from time import sleep
from datetime import datetime

currency_list = ['PLN', 'CHF', 'EUR', 'USD', 'JPY', 'CAD']
BASE = 'http://127.0.0.1:5000/'
resource_payer = 'payer/'
resource_transaction = 'transaction/'
trac_count = 100

def get_transaction_details():
    transaction_id = str(uuid4())
    payer_id = str(uuid4())[:13 ]
    amount = round(uniform(-10000, 10000), 2)
    currency = choice(currency_list)
    time = datetime.strptime(str(datetime.now())[:19], '%Y-%m-%d %H:%M:%S')
    sleep(0.2)
    return transaction_id, payer_id, amount, currency, time

def generate_transaction(transaction_count):
    for _i in range(transaction_count):
        yield get_transaction_details()

def main():
    for transaction in generate_transaction(trac_count):
        response1 = requests.post(BASE + resource_payer + transaction[1], params={'http':'','https':''})
        response2 = requests.post(BASE + resource_transaction + transaction[0], params={'http': '', 'https': '', 'amount': transaction[2], 'currency': transaction[3], 'time': transaction[4], 'payer_id': randrange(1,trac_count+1)})
        print(response2.json())

if __name__ == '__main__':
    main()
