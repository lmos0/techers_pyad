# Função que verifica se um número é maior, menor ou igual a outro.

def maior_menor_igual(x,y):
    # x: o primeiro número/primeiro argumento
    # y: o segundo número/segundo argumento

    #retorno: um texto informando se x é maior, menor ou igual a y.
    # Quando a função retorna um valor. ela PARA a execução
    if x > y:
        return f"{x} é maior do que {y}"
    elif x < y:
        return f"{x} é menor do que {y}"
    else:
        return f"{x} é igual a {y}"
    

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input("Digite o segundo número: "))



resultado = maior_menor_igual(numero1,numero2)
print(resultado)