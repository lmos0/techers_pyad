# Função que verifica se um número é positivo ou negativo.
# Vai receber um numero como argumento
# Retornar uma string falando se o número é positivo ou negativo

def positivo_negativo(numero):
    if numero > 0:
        return f"{numero} é positivo"
    elif numero < 0:
        return f'{numero} é negativo'
    else:
        return f"{numero} é zero"

numero = int(input("Digite um número: "))
resultado = (positivo_negativo(numero))

print(resultado)