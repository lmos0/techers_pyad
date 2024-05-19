password = 'coxinha_123'

while True:
    typed_password = input('Favor digitar a senha: ')
    if password == typed_password:
        print('Acesso permitdo')
        break
    else:
        print('Acesso negado')

