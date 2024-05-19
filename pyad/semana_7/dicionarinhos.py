def main():
  # Pede ao usuário uma lista de produtos
  produtos = input("Digite uma lista de produtos separados por vírgula: ").split(",")

  # Cria um dicionário com os preços dos produtos
  precos = {"banana": 1.00, "maçã": 2.00, "abacaxi": 3.00, "melancia": 4.00}

  # Calcula o preço total da compra
  preco_total = 0
  for produto in produtos:
    if produto in precos:
      preco_total += precos[produto]
    else:
      print(f"O produto {produto} não está na lista de preços.")

  # Imprime o preço total da compra
  print(f"O preço total da compra é: R${preco_total:.2f}")

if __name__ == "__main__":
  main()
