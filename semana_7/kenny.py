import requests

url = 'https://api.kanye.rest/'

resposta = requests.get(url)
print(resposta.status_code)
print(resposta.json()['quote'])