

# def teste_quadrado():
#     if quadrado(2) != 4:
#         print('Erro. 2 ao quadrado deveria ser 4')
#     if quadrado(3) != 9:
#         print('Erro. 3 ao quadrado deveria ser 9')

##############################################################
# def teste_quadrado():
#     try:
#         assert quadrado(2) == 4
#     except AssertionError:
#         print('2 ao quadrado não deu 4')
#     try:
#         assert quadrado(3) == 9
#     except AssertionError:
#         print('3 ao quadrado não deu 9')
#     try:
#         assert quadrado(-2) == 4
#     except AssertionError:
#         print('O quadrado de -2 não deu 4')
#     try:
#         assert quadrado(0) == 0
#     except AssertionError:
#         print('O quadrado de zero não deu zero')
###################################################
from calculadora import quadrado


def main():
    teste_quadrado_positivo()
    teste_quadrado_negativo()
    teste_quadrado_zero()

def teste_quadrado_positivo():
    assert quadrado(2) == 4
    assert quadrado(3) == 9

def teste_quadrado_negativo():
    assert quadrado(-2) == 4
    assert quadrado(-3) == 9

def teste_quadrado_zero():
    assert quadrado(0) == 0


if __name__ == "__main__":
    main()