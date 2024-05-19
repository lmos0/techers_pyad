#Criar um programa em que o usuário cadastre um nome e um endereço de email vinculado aquele nome (chave:valor)
# Usuário consultar o endereço do e-mail do usuário, digitando apenas o nome
# input: caio
# retorno: caio@gmail.com

cadastros = {}

while True:
    nome = input('Digite um nome (ou digite "sair" para encerrar) ').lower()
    if nome == 'sair':
        break
    email = input('Digite o endereço de e-mail ')
    cadastros[nome] = email

nome_consulta = input('Digite o nome a ser consultado ').lower()
email = cadastros.get(nome_consulta, 'Nome não encontrado')
print(f'Endereço de e-mail de {nome_consulta} : {email}')
