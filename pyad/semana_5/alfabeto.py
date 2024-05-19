nomes = []

with open('nomes.txt') as arquivo:
    for linha in arquivo:
        nomes.append(linha.rstrip())

with open('nomes_alfabeto.txt', 'a') as arquivo:
    for nome in sorted(nomes):
        arquivo.write(str(nomes))