def contador_de_palavra(caminho_do_arquivo):
    contagem_palavras = {}
    
    arquivo = open(caminho_do_arquivo, encoding="utf-8")
    for linha in arquivo:
         print(linha.rstrip())
         for palavra in linha.split(' '):
            palavra = palavra.strip('.,!?:;"').lower()
            contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    arquivo.close()
    return(contagem_palavras)

def main():
    caminho_do_arquivo = 'texto.txt'
    palavras_contadas = contador_de_palavra(caminho_do_arquivo)
    print('Palavra: ')
    for palavra, numero in  palavras_contadas.items():
        print(f'{palavra}: {numero}')

main()           

