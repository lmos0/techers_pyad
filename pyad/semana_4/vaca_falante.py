import random

def boas_vindas():
    print('Bem-vindo ao jogo! ')
    print('Tente advinhar o número que estou pensando')

def sortear_numero():
    return random.randint(1,100)

def advinhar_numero():
    numero_sorteado = sortear_numero()
    tentativas = 0

    while True:
        chute = int(input('Digite um número: '))
        tentativas += 1
        if chute == numero_sorteado:
            print(f'Parabéns você acertou em {tentativas} tentativas')
            break
        elif chute < numero_sorteado:
            print('Tente um número maior')
        else:
            print('Tente um número menor')

boas_vindas()
advinhar_numero()