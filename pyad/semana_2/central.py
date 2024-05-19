print('Bem vindo à nossa central de atendimento!')
print('Digite 1 para reclamações')
print('Digite 2 para elogios')
print('Digite 3 para sugestões')
print('Digite 4 para falar com atendente')

opcao = int(input('Digite a opção desejada '))

if opcao == 1:
    print('Setor de Reclamações ')

elif opcao == 2:
    print('Deixe aqui seu elogio! ')

elif opcao == 3:
    print('Sugestões')

elif opcao == 4:
    print('Redirecionando para um atendente')

else:
    print('opção inválida!')
