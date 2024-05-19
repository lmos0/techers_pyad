#Crie um programa que lê um arquivo CSV, filtra os dados por uma coluna específica e imprime os resultados na tela.

import csv

def filtrar_por_nome(arquivo_csv, nome):
    with open(arquivo_csv, newline='') as csvfile:
        leitor_csv = csv.DictReader(csvfile)
        for linha in leitor_csv:
            if linha['nome'] == nome:
                print('Nome: ', linha['nome'])
                print('Idade:', linha['idade'])
                print('Email', linha['email'])
                print()

arquivo_csv = 'cadastro.csv'
nome_para_filtrar = 'Maria'

filtrar_por_nome(arquivo_csv, nome_para_filtrar)
