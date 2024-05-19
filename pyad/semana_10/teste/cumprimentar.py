def main():
    nome = input('Qual seu nome: ')
    print(ola(nome))



def ola(nome="usuario"):
    return f"Bom dia, {nome}"


if __name__ == "__main__":
    main()

#funções retorno ou eles geram side effects (efeitos colaterais), efeitos na tela = print 
#evitar ao máximo usar print e side effects em geral. O idea é dar prioridade ao retorno 