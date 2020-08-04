import requests

BASE = 'http://127.0.0.1:5000/'
resource = 'item/'
resource_item = 'chair3'
resource_item2 = 'tablet'

def handle_reuqest():
    response = requests.post(BASE + resource + resource_item, params={'http':'','https':'','price':12.00})
    response = requests.get(BASE + resource + resource_item, params={'http':'','https':''})
    print(response.json())
    response = requests.post(BASE + resource + resource_item2, params={'http':'','https':'','price':120.00})
    response = requests.get(BASE + resource + resource_item2, params={'http':'','https':''})
    print(response.json())

def main():

    handle_reuqest()

if __name__ == '__main__':
    main()
