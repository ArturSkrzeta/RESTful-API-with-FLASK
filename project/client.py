import requests

BASE = 'http://127.0.0.1:5000/'
resource_owner = 'owner/'
resource = 'item/'
resource_item = 'chair'
resource_item2 = 'tablet'

def handle_reuqest():

    response = requests.post(BASE + resource_owner + 'Artur', params={'http':'','https':''})
    print(response.json())
    response = requests.post(BASE + resource + resource_item, params={'http':'','https':'','price':12.00, 'owner_id':1})
    response = requests.get(BASE + resource + resource_item, params={'http':'','https':''})
    print(response.json())
    response = requests.post(BASE + resource + resource_item2, params={'http':'','https':'','price':120.00, 'owner_id':1})
    response = requests.get(BASE + resource + resource_item2, params={'http':'','https':''})
    print(response.json())
    response = requests.get(BASE + resource_owner + 'Artur', params={'http':'','https':''})
    print(response.json())

def main():
    handle_reuqest()

if __name__ == '__main__':
    main()
