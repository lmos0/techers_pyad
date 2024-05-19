idade = int(input('Digite sua idade: '))
profissao = input('Digite sua profissão: ')

if idade <= 21 or profissao == 'estudante' or profissao == 'professor':
    print('Você pode fazer a assinatura gratuita')
else:
    print('Você não pode fazer a assinatura gratuita')
