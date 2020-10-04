# testing HTTP methods
# on RESTful FLASK API

import requests

BASE = 'http://127.0.0.1:5000/'
resource_payer = 'payer/'
payer = 'Artur'
resource = 'transaction/'
transaction_name = 'laptop HP'
second_transaction_name = 'laptop Apple'
new_amount = 100.00

method_responses = {
    'post': {'name': transaction_name, 'amount': 12.00},
    'get_before': {'name': transaction_name, 'amount': 12.00},
    'put': {'name': transaction_name, 'amount': new_amount},
    'delete': {'message': 'Transaction deleted.'},
    'get_after': {'message': 'Transaction not found'},
    'post_second': {'name': second_transaction_name, 'amount': 50.00}
}

def print_response(response):
    print('\n')
    print(response.json())

def test_methods():

    response = requests.post(BASE + resource + transaction_name, params={'http':'','https':'','amount':12.00, 'currecnt:'PLN', 'time':'2020-08-06 11:50:36' payer_id':1})
    assert response.json() == method_responses['post']

    response = requests.get(BASE + resource + transaction_name)
    assert response.json() == method_responses['get_before']

    response = requests.put(BASE + resource + transaction_name, params={'http':'', 'https':'','amount':new_amount, 'payer_id':1})
    assert response.json() == method_responses['put']

    response = requests.delete(BASE + resource + transaction_name, params={'http':'', 'https':''})
    assert response.json() == method_responses['delete']

    response = requests.get(BASE + resource + transaction_name, params={'http':'', 'https':''})
    assert response.json() == method_responses['get_after']

    response = requests.put(BASE + resource + second_transaction_name, params={'http':'', 'https':'','amount':50.00, 'payer_id':1})
    assert response.json() == method_responses['post_second']

def main():
    test_methods()

if __name__ == "__main__":
    main()
