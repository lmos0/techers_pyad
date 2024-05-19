#Lista com nomes pré-determinado 
lista_de_casamento = ['Amanda', 'Pamela', 'Dani', 'Mauricio', 'Hiago', 'Luis', 'Edgar']

#Por meio de input, seu programa vai procurar o nome da pessoa e dizer se ela está convidada ou não.

searched_name = input('Entre com o nome do convidado ').title()

# Se programa achar o nome da pessoa lista, ele printa 'essa pessoa está na lista'
if searched_name in lista_de_casamento:
    print(f'{searched_name} está na lista ')
#Caso contrário, penetra detecado 
else:
    print('Não está na lista! ')

