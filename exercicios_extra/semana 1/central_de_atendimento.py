# Description: Exemplo de uso de if, elif e else
print("Bem vindo à nossa central de atendimento")
print("Digite 1 para reclamações")
print("Digite 2 para elogios")
print("Digite 3 para sugestões")
print("Digite 4 para falar com o atendente")
opcao = int(input("Digite a opção desejada: "))
if opcao == 1:
    print("Reclamações")
elif opcao == 2:
    print("Elogios")
elif opcao == 3:
    print("Sugestões")
elif opcao == 4:
    print("Atendente")
else:
    print("Opção inválida")
