import requests

titulo = input('Digite o nome do filme: ').title()

url = f"http://www.omdbapi.com/?t={titulo}&apikey=84a1f976"

resposta = requests.get(url)
print(resposta.status_code)
data = resposta.json() #converte a resposta em um dicionário do python

if data["Response"] == "True":



    print('Título:', data['Title'] )
    print('Ano:', data['Year'] )
    print('Nota IMDB', data['imdbRating'] )
    print("Diretor:", data['Director'])
    print('Genêro', data['Genre'])

else:
    print("Filme não encontrado ou servidor fora do ar!" )