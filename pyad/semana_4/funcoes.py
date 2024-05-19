variavel_global = 'oi, eu sou uma variável global '
def main():
    contar_carneiros(7)



def contar_carneiros(qtde=3):
    for _ in range(qtde):
        print('🐏')


#bloco de código reutilizável o qual executa uma função específica 

def potencia_de_dois(n):
    potencia = n ** 2
    return potencia

def escopo():
    variavel_local = 'oi, sou uma variável local'
    
   
if __name__ == "__main__":
    main()

