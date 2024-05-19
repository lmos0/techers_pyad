def maior_menor_igual(x, y):
  """
  Função que verifica se um número é maior, menor ou igual a outro.

  Argumentos:
    x: O primeiro número.
    y: O segundo número.

  Retorno:
    Uma string que indica se x é maior, menor ou igual a y.
  """
  if x > y:
    return f"{x} é maior que {y}"
  elif x < y:
    return f"{x} é menor que {y}"
  else:
    return f"{x} é igual a {y}"

# Exemplo de uso
# numero1 = int(input("Digite o primeiro número: "))
# numero2 = int(input("Digite o segundo número: "))

# resultado = maior_menor_igual(numero1, numero2)

# print(resultado)

def positivo_negativo(numero):
  """
  Função que verifica se um número é positivo ou negativo.

  Argumentos:
    numero: O número a ser verificado.

  Retorno:
    Uma string que indica se o número é positivo ou negativo.
  """
  if numero > 0:
    return f"{numero} é positivo"
  else:
    return f"{numero} é negativo"

# Exemplo de uso
numero = int(input("Digite um número: "))

resultado = positivo_negativo(numero)

print(resultado)
