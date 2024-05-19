#Crie um programa que abre um arquivo (.txt), escreve uma mensagem nele e o fecha.

def escrever_arquivo(nome_arquivo, mensagem):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(mensagem)
        print("Mensagem escrita no arquivo com sucesso!")

nome_arquivo = 'mensagem.txt'
mensagem = "Tomar energético demais causa taquicardia "
escrever_arquivo(nome_arquivo, mensagem)