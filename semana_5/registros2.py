nome = input('Digite seu nome: ')

with open("nomes2.txt","a") as arquivo:
    arquivo.write(f'{nome}\n')