#Crie uma função que receba um nome e imprima uma saudação personalizada.
def saudacao_personalizada(nome):
    mensagem = f"Olá, {nome}. Seja bem-vindo!"
    print(mensagem)

# banana = input('Digite seu nome: ')

#Crie uma função que encontre o maior valor em uma lista de números.
    
def encontrar_maior_valor(lista_de_numero):
    maior_valor = None
    for numero in lista_de_numero:
        if maior_valor is None or numero > maior_valor:
            maior_valor = numero
    return maior_valor

listinha_de_numero = [3,2,5,1,99,88]
listinha_de_numero2 = [343,454,322,858,31120,34323]
# valor_encontrado = encontrar_maior_valor(listinha_de_numero2)
# print(f"O maior valor encontrado na lista é: {valor_encontrado}")


#Crie uma função que imprima os números de 1 a 100, mas substitua os múltiplos de 3 pela palavra "Fizz" 
#e os múltiplos de 5 pela palavra "Buzz”

def fizzbuzz():
    for numero in range(1,101):
        if numero % 3 == 0:
            print("Fizz!")
        elif numero % 5 == 0:
            print("Buzz")
        else:
            print(numero)


def fizzbuzz2():
    for numero in range(1,101):
        if numero % 3 == 0 and numero % 5 == 0:
            print("FizzBuzz")
        elif numero % 3 == 0:
            print("Fizz!")
        elif numero % 5 == 0:
            print("Buzz")
        else:
            print(numero)

fizzbuzz2()