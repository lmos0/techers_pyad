def main():
    palavra1 = input("Digite a primeira string ")
    palavra2 = input('Digite a segunda string ')
    texto = input("Digite um texto: ")
    print(caixa_alta(texto))
    print(concatenar_strings(palavra1,palavra2))
    

def caixa_alta(texto):
    return texto.capitalize()

def concatenar_strings(txt1,txt2):
    return txt1 + txt2

if __name__ == "__main__":
    main()