import requests

#Get 
#status http
# 200:ok
# 300: conteúdo redirecionado
# 400: erro cliente (404, conteúdo não encontrado)
# 500: falha no servidor


cep = input('Digite seu CEP: ')
url = f'https://viacep.com.br/ws/{cep}/json/'

resposta = requests.get(url)
print(resposta.status_code)
print(resposta.json()) #transformando minha resposta em um dicionário
print('Rua: ', resposta.json()['logradouro'])
print('Bairro: ', resposta.json()['bairro'])
print(resposta.json()['localidade'])
print(resposta.json()['uf'])
print(resposta.json()['cep'])