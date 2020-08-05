# testing HTTP methods
# on RESTful FLASK API

import requests

BASE = 'http://127.0.0.1:5000/'
resource_owner = 'owner/'
owner = 'Artur'
resource = 'item/'
item_name = 'laptop HP'
second_item_name = 'laptop Apple'
new_price = 100.00

method_responses = {
    'post': {'name': item_name, 'price': 12.00},
    'get_before': {'name': item_name, 'price': 12.00},
    'put': {'name': item_name, 'price': new_price},
    'delete': {'message': 'Item deleted.'},
    'get_after': {'message': 'Item not found'},
    'post_second': {'name': second_item_name, 'price': 50.00}
}

def print_response(response):
    print('\n')
    print(response.json())

def test_methods():

    response = requests.post(BASE + resource + item_name, params={'http':'','https':'','price':12.00, 'owner_id':1})
    assert response.json() == method_responses['post']

    response = requests.get(BASE + resource + item_name)
    assert response.json() == method_responses['get_before']

    response = requests.put(BASE + resource + item_name, params={'http':'', 'https':'','price':new_price, 'owner_id':1})
    assert response.json() == method_responses['put']

    response = requests.delete(BASE + resource + item_name, params={'http':'', 'https':''})
    assert response.json() == method_responses['delete']

    response = requests.get(BASE + resource + item_name, params={'http':'', 'https':''})
    assert response.json() == method_responses['get_after']

    response = requests.put(BASE + resource + second_item_name, params={'http':'', 'https':'','price':50.00, 'owner_id':1})
    assert response.json() == method_responses['post_second']

def main():
    test_methods()

if __name__ == "__main__":
    main()
