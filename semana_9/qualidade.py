#synta error

#Runtime Erros => Erros que acontecem durante a execução do código. Geralmente, são comportamentos anômalos decorrentes de ações inesperadas do usuário

def main():
    x = pegar_numero()
    print(f'x é {x}')


 

def pegar_numero():
    while True:
        try:
           return float(input('Digite o valor de X: '))   
        except ValueError:
            pass
        
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
main()