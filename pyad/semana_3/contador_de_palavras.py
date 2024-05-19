frase = input('Digite seu texto ')

palavras = frase.split()

frase_freq = {}

for palavra in palavras:
    if palavra in frase_freq:
        frase_freq[palavra] += 1
    else:
        frase_freq[palavra] = 1

print("A frequência das palavras é: ")
for palavra, freq in frase_freq.items():
    print(palavra + ":", freq)
