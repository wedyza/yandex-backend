import requests

BASE_URL = 'https://fakestoreapi.com/'

#1
response = requests.get(f'{BASE_URL}/products').json()
answer = list()
for product in response:
    if product['price'] < 20:
        answer.append(product)
# print(answer)

#2
response = requests.get(f'{BASE_URL}/products/categories').json()
# print(response)

#3 
category = 'jewelery'
response = requests.get(f'{BASE_URL}/products/category/{category}').json()
# print(response)

#4
response = requests.get(f'{BASE_URL}/users').json()
# print(response)

#5
response = requests.post(f'{BASE_URL}/users', json={
    'email' : 'wedyza@mail.ru',
    'username' : 'wedyzza',
    'password' : 'zxcqwe',
    'name' : {
        'firstname' : 'Kostya',
        'lastname' : 'Gavrilov'
    },
    'address' : {
        'city' : 'Ekaterinburg',
        'street' : '100 years university',
        'number' : 6,
        'zipcode' : '1234-1234',
        'geolocation' : {
            'lat' : '-37.3159',
            'long' : '81.1496'
        }
    },
    'phone' : '+78922345721'
})
print(response.json())
