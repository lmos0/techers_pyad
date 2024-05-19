def main():
    x = int(input('Digite o valor de x: '))
    print("X ao quadrado é", quadrado(x))

def quadrado(n):
    return n * n 

if __name__ == "__main__":
    main()

#Arquivo com operações matemáticas

# Escrever duas funções somar e subtrair. A função vai receber dois argumentos somar(arg1,arg2) e subtrair(arg1,arg2)
# como o retorno vocês vão testar se os resultados batem

# 4+5 = 9
# 36+36 = 72

# 4 - 8 = -4

#Façam a calculadora falhar em pelo menos um teste


#Pra rodar pytest. Abra terminar e digite: 
# pytest  nome_do_arquivo.py