# vermelho: é para parar
# amarelo: atenção
# verde: siga

# O usuário vai digitar a cor do semáforo e o programa vai dizer a mensagem referente àquela cor. Caso o usuário não digite uma cor válida, o programa informará o usuário.

cor = input("Digite a cor: ")


if cor.lower() == "vermelho":
    print("PARE!")

elif cor.lower() == "amarelo":
    print("CUIDADO")

elif cor.lower() == "verde":
    print("SIGA")

else:
    print("Cor Inválida")
