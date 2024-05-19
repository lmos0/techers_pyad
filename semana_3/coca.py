coke = 100
coins = [10,25,50]

while coke > 0:
    print(f'Faltam ainda {coke} centavos: ', )
    payment = int(input('Insira uma moeda '))
    if payment in coins:
        coke = coke - payment
        print(f'Faltam ainda {coke} centavos: ')
    elif payment not in coins:
        print('Valor inválido. Insira uma moeda de 10, 25 ou 50 ')
    
    if coke <= 0:
        change = abs(coke)
        print('Seu troco é ', coke)
        print('Aqui está sua coca')
        break