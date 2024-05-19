# Escrever um programa que calcula desconto. Por regra, ele dá 5% desconto em todas as compras. Contudo, se o valor da compra for MAIOR que R$ 100,00, o desconto será de 10%.
# Novo valor do produto com desconto

# pseudocódigo
# 1 - Pegar o valor da compra com usuário
# 2 - Ele tem que checar se ele valor é menor que 100
# 3 - Caso seja menor que 100, informe ao cliente que ele tem 5% de desconto
# 4 - caso contrário, dê 10% de desconto
# 5 - mostre para o usuário o valor do produto com desconto JÁ calculado

valor_da_compra = float(input("Digite o valor total da sua compra: "))
if valor_da_compra < 100:
    desconto = valor_da_compra * 0.05
else:
    desconto = valor_da_compra * 0.10

valor_com_desconto = valor_da_compra - desconto
print(f"o valor do produto agora é {valor_com_desconto}")
print("o valor do produto com desconto agora é", valor_com_desconto)

# Escrevam um programa que irá determinar se um ano é bissexto ou não. Pegar pegar o valor do ANO e dividir por 4, se for disível por 4, mas não for divisel por 100 -> é porque o ano bissexto.
# Se você dividir o ano por 400, se for divisel (não sobrar resto) é porque ele bissexto
