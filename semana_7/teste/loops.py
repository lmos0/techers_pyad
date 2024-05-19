def countdown(n):
    """Função para contar regressivamente de um número até zero."""
    while n >= 0:
        print(n)
        n -= 1

# Solicita ao usuário um número inteiro positivo
#numero = int(input("Digite um número inteiro positivo para iniciar a contagem regressiva: "))

# Chama a função de contagem regressiva
#countdown(numero)

def tabuada(numero):
  """
  Função que imprime a tabuada de um número usando while.

  Argumentos:
    numero: O número cuja tabuada será impressa.

  Retorno:
    Nenhum.
  """

  # Contador
  i = 1

  # Imprime o cabeçalho da tabuada
  print(f"Tabuada do {numero}")

  # Loop while para imprimir cada linha da tabuada
  while i <= 10:
    # Calcula o resultado da multiplicação
    resultado = numero * i

    # Imprime a linha da tabuada
    print(f"{numero} x {i} = {resultado}")

    # Incrementa o contador
    i += 1

# Exemplo de uso
numero = int(input("Digite um número: "))

tabuada(numero)
