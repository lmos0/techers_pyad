idade = int(input('Digite sua idade: '))
cnh = input('Você tem CNH? (S/N)').upper()

if idade >= 18 and cnh == 'S':
    print('Você pode dirigir ')
else:
    print('Você não pode dirigir! ')
