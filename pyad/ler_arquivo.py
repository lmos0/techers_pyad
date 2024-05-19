#Crie um programa que abre um arquivo usando with(), lê seu conteúdo e o imprime na tela.

def ler_aquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print('Conteúdo do arquivo é', conteudo)

nome_arquivo = 'mensagem.txt'

ler_aquivo(nome_arquivo)