idade = int(input('Digite sua idade: '))
profissao = input('Digite sua profissão: ').upper().strip()

if idade <= 21 or profissao == 'ESTUDANTE' or profissao == 'PROFESSOR':
    print('Você pode fazer a assinatura gratuitamnte')

else:
    print('Você não pode fazer assinatura!')
