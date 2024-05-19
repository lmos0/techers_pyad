def somar(x,y):
    resultado = x + y
    print(resultado)

def raiz_quadrada(x):
    pass


soma = lambda x,y: x+y
# print(soma(3,3))

#Uma das principais razões para se utilizar o lambda é passar uma função como argumento dentro de outra função!

numeros = [1,2,3,4,5]

pares = filter(lambda x : x % 2 == 0, numeros)
print(list(pares))
