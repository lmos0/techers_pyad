# Escrevam um programa que irá determinar se um ano é bissexto ou não. Pegar pegar o valor do ANO e dividir por 4, se for disível por 4, mas não for divisel por 100 -> é porque o ano bissexto.
# Se você dividir o ano por 400, se for divisel (não sobrar resto) é porque ele bissexto

ano = int(input('Digite o ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é bissexto")

else:
    print(ano, "não é bissexto")