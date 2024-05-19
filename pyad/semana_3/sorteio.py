import random 

lista_de_nomes = []

while True:
    acao = input('Digite 0 para adicionar um nome, digite 1 para sortear um nome, digite 2 para encerrar o programa, digite 3 para remover um nome da lista: ' )
    if acao == '0':
        nome = input('Digite nome a ser inserido: ')
        lista_de_nomes.append(nome)
        print('Atualmente há na lista ', lista_de_nomes)
    elif acao == '1':
        if lista_de_nomes:
            nome_aleatorio = random.choice(lista_de_nomes)
            print('O sorteado foi ', nome_aleatorio )
        else:
            print('A lista está vazia ')
    elif acao == '2':
        break
    elif acao == '3':
        if lista_de_nomes:
            print('Atualmente há na lista ', lista_de_nomes)
            nome_a_ser_removido = input('Nome a ser removido da lista: ')
            lista_de_nomes.remove(nome_a_ser_removido)
            print(lista_de_nomes)
        else:
            print('lista vazia! ')

    else:
        print('Comando inválido.')




