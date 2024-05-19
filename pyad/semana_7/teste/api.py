import requests
import json

cep = input('Digite o CEP: ')
url = f'https://viacep.com.br/ws/{cep}/json/'

response = requests.get(url)
print(response.status_code)
print(response.json())
print(response.json()['logradouro'])
print(response.json()['bairro'])
print(response.json()['localidade'])
print(response.json()['uf'])
print(response.json()['cep'])
