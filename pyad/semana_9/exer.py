
# while True:
#     try:
#         num1 = float(input('Digite um número '))
#         num2 = float(input('Digite um outro número '))

#         resultado = num1 / num2
#         print(resultado)
#         break
#     except ValueError:
#         print('Erro: Não é possível efetuar um divisão por zero')
    

#ZeroDivisionError: erro ao dividir valor por zero
#NameError: variável não declarada
#ValueError: tipo de dado incompatível com a operação
#IndexError: quando se tenta acessar um index não existente dentro de uma lista/array

lista = [1,2,3,4,5]

try:
    indice = int(input('Digite a posição do elemento que você quer acessar dentro da lista: '))
    elemento = lista[indice]
    print(f'Elemento na posição {indice} é {elemento}')

except ValueError:
    print('Erro: Você não digitou um número inteiro!')

except IndexError:
    print('Erro: Não há nenhum elemento na posição digitada!')