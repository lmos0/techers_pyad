import random

palavras = ['caneca', 'livros', 'lampada', 'monitor', 'roteador', 'programacao', 'mouse',
            'agua', 'enciclopedia', 'smartphone', 'oculos', 'cafe', 'energetico', 'raquete', 'miojo']


def escolher_palavra():
    return random.choice(palavras)

def mostrar_forca(palavra,letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end='')
        else:
            print('_', end='')
    print()

def jogar():
    palavra = escolher_palavra()
    letras_corretas = []
    tentativas = 6

    print('Bem-vindo ao jogo da forca')
    mostrar_forca(palavra, letras_corretas)

    while tentativas > 0:
        letra = input('digite uma letra: ').lower()

        #cheque se o input do usuário é somente uma letra e se não é um numeral
        if len(letra) != 1 or not letra.isalpha():
            print('Por favor, digite apenas uma LETRA!')
            continue

        if letra in letras_corretas:
            print('Você tentou essa letra. Tente outra!')
            continue
        if letra in palavra:
            letras_corretas.append(letra)
            print('Correto! ')
        else:
            tentativas -= 1
            print(f'Incorreto! Você tem {tentativas} tentativas restantes. ')

        mostrar_forca(palavra, letras_corretas)

        if all(letra in letras_corretas for letra in palavra):
            print('Você ganhou!')
            break
    
    else:
        print(f'Você perdeu! A palavra era {palavra} ')

jogar()
