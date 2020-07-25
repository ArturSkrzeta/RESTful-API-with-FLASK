# testing HTTP methods
# on RESTful FLASK API

import requests

BASE = 'http://127.0.0.1:5000/'
endpoint = 'item/'
item_name = 'chair'
second_item_name = 'table'
new_price = 100

method_responses = {
    'post': {'name': item_name, 'price': 12.0},
    'get_before': {'item': {'name': item_name, 'price': 12.0}},
    'put': {'name': item_name, 'price': new_price},
    'delete': {'message': 'Item deleted'},
    'get_after': {'item': None},
    'post_second': {'name': second_item_name, 'price': 50.0}
}

def print_response(response):
    print('\n')
    print(response.json())

def test_methods():

    response = requests.post(BASE + endpoint + item_name, params={'http':'','https':'','price':12})
    assert response.json() == method_responses['post']

    response = requests.get(BASE + endpoint + item_name)
    assert response.json() == method_responses['get_before']

    response = requests.put(BASE + endpoint + item_name, params={'http':'', 'https':'','price':new_price})
    assert response.json() == method_responses['put']

    response = requests.delete(BASE + endpoint + item_name, params={'http':'', 'https':''})
    assert response.json() == method_responses['delete']

    response = requests.get(BASE + endpoint + item_name, params={'http':'', 'https':''})
    assert response.json() == method_responses['get_after']

    response = requests.put(BASE + endpoint + second_item_name, params={'http':'', 'https':'','price':50})
    assert response.json() == method_responses['post_second']

def test_get_all_items():

    response = requests.get(BASE + '/items')
    assert response.json() == {'items': [method_responses['post_second']]}

def main():
    test_methods()
    test_get_all_items()

if __name__ == "__main__":
    main()
