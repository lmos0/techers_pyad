#definir uma lista ex:[2,3,6,5]. 
#Imprima a soma de todos os elementos da lista
lista = [3,5,7,1,2,9,9,3,10]

def soma_lista(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma


total_da_lista = soma_lista(lista)
print(f'O valor total da lista é: {total_da_lista}')

def media_lista(lista):
    soma = 0
    for elemento in lista:
        soma += elemento 
    return soma / len(lista)

resultado_da_media = media_lista(lista)
print(f'A média da lista é {resultado_da_media}')

nome = "luis marcio"
print(len(nome))

lista1 = ['elton','luis','caio']
lista2 = [4,'true',6]
lista3 = lista1 + lista2
print(lista3)

# Criar uma função pra percorrer uma lista e falar qual é o maior valor na lista

def maior_na_lista(lista):
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

maior_valor = maior_na_lista(lista)
print(f'o maior elemento da lista é {maior_valor}')

