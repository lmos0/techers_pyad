#Criar um programa em que o usuário cadastre um nome e um endereço de email vinculado aquele nome (chave:valor)
# Usuário consultar o endereço do e-mail do usuário, digitando apenas o nome
# input: caio
# retorno: caio@gmail.com
candidatos = {}

while True:
    print("1 - Para adicionar um novo candidato: ")
    print("2 - Para votar em um candidato registrado ")
    print("3 - Para mostrar resultados parciais ")
    print("4 - Encerrar a votação")

    escolha_do_usuario = input('Escolha uma opção: ')

    if escolha_do_usuario == "1":
        nome_do_candidato = input("Digite o nome do seu candidato: ").lower()
        candidatos[nome_do_candidato] = 0
        print("Candidato: ",  nome_do_candidato, "adicionado com sucesso")
        print()

    elif escolha_do_usuario == "2":
        nome_do_candidato = input("Digite o nome do seu candidato: ").lower()
        if nome_do_candidato in candidatos:
            candidatos[nome_do_candidato] += 1
            print(f"Voto no candidato {nome_do_candidato} confirmado!")
        else:
            print("Candidato não encontrado")

    elif escolha_do_usuario == "3":
        print("Candidato\tVotos")
        for candidato, votos in candidatos.items():
            print(candidato + ":\t" + str(votos))
    
    elif escolha_do_usuario == "4":
        print("Votação Encerrada ")
        break

    else:
        print("opção inválida")
    
    



    

