# with open('nomes.txt', 'r') as arquivo:
#     linhas = arquivo.readlines()

# for linha in linhas:
#     print('olá', linha.rstrip())

with open('nomes.txt') as arquivo:
    for linha in arquivo:
        print('olá', linha.rstrip())