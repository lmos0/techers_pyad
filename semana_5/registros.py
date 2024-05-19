while True:

    nome = input('Digite seu nome:  (ou digite "sair")')

    if nome == "sair":
        break

    arquivo = open('nomes.txt',"a")
    arquivo.write(f"Olá, {nome}\n")
    arquivo.close()