"""Função para contar regressivamente de um número até zero."""

import time

def contagem_regressiva(n):
    for i in range(n,-1, -1):
        print(n)
        n -= 1
        time.sleep(1)
        
    
numero = int(input('Digite um número inteiro positivo para iniciar a contagem regressiva: '))
contagem_regressiva(numero)

# for in range