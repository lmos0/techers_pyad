import random 

def adicionar_nomes(lista_de_nomes):
    nome = input('Digite nome a ser inserido: ')
    lista_de_nomes = lista_de_nomes.append(nome)

def remover_nomes(lista_de_nomes):
    if lista_de_nomes:
        print("Atualmente há na lista", lista_de_nomes) 
        nome_removido = input('Digite o nome a ser removido')
        if nome_removido in lista_de_nomes:
            lista_de_nomes.remove(nome_removido)
        else:
            print('Nome não encontrado')

def sortear_nomes(lista_de_nomes):
    if lista_de_nomes:
        nome_aleatorio = random.choice(lista_de_nomes)
        print('Nome sorteado foi ', nome_aleatorio)
    else:
        print('Lista vazia')

def encerrar_programa():
    return True

def main():
    lista_de_nomes = []

    while True:
        acao = input('Pressione "0" para adicionar um nome. Pressione "1" para remover um nome. Pressione "2" para sortear um nome. Pressione "3" para encerrar o programa ')
        if acao == '0':
            adicionar_nomes(lista_de_nomes)
        elif acao == '1':
            remover_nomes(lista_de_nomes)
        elif acao == '2':
            sortear_nomes(lista_de_nomes)
        elif acao == '3':
            if encerrar_programa():
                print('Programa encerrado')
                break
           
        else:
            print("Comando inválido. Digite outra vez")

if __name__ == "__main__":
    main()