with open('paises.csv', encoding="utf8") as arquivo:
    for linha in arquivo:
        pais, continente = linha.rstrip().split(',')
        print(f'{pais} está na {continente}')



     