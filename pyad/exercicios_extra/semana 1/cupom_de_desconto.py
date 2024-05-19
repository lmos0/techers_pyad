total_compra = float(input("Digite o valor total da compra: "))
cupom_de_desconto = input("Você tem cupom de desconto? (S/N): ")

desconto_promocao = 0.10
desconto_cupom = 0.05

valor_final = total_compra

if total_compra >= 50 or cupom_de_desconto == 'S':
    if total_compra >= 50:
        valor_final = total_compra - (total_compra * desconto_promocao)
        print(
            f"Você ganhou um desconto de 10% na sua compra. O valor final é R${valor_final:.2f}")
    elif cupom_de_desconto == 'S':
        valor_final = total_compra - (total_compra * desconto_cupom)
        print(
            f"Você ganhou um desconto de 5% na sua compra. O valor final é R${valor_final:.2f}")
else:
    print(f"O valor final é R${valor_final:.2f}")
