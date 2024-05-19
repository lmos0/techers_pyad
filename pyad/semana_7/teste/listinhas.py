def mais_longo():
    # Pede ao usuário uma lista de palavras
  palavras = input("Digite uma lista de palavras separadas por vírgula: ").split(",")

  # Inicializa a variável que armazenará a palavra mais longa
  palavra_mais_longa = ""

  # Percorre a lista de palavras
  for palavra in palavras:
    # Se a palavra atual for mais longa que a palavra mais longa
    if len(palavra) > len(palavra_mais_longa):
      # Atualiza a palavra mais longa
      palavra_mais_longa = palavra

  # Imprime a palavra mais longa
  print(f"A palavra mais longa é: {palavra_mais_longa}")

def soma_lista(lista):
  soma = 0
  for elemento in lista:
    soma += elemento
  return soma

# lista = [1, 2, 3, 4, 5,11]
# soma = soma_lista(lista)
# print(f"A soma da lista é: {soma}")

def media_lista(lista):
  soma = 0
  for elemento in lista:
    soma += elemento
  return soma / len(lista)

lista = [1, 2, 3, 4, 5]
media = media_lista(lista)
print(f"A média da lista é: {media}")

def maior_lista(lista):
  maior = lista[0]
  for elemento in lista:
    if elemento > maior:
      maior = elemento
  return maior

lista = [1, 2, 3, 4, 5]
maior = maior_lista(lista)
print(f"O maior elemento da lista é: {maior}")