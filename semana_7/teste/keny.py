import requests
import json

url = 'https://api.kanye.rest/'

response = requests.get(url)
print(response.status_code)
print(response.json())
print(response.json()['quote'])