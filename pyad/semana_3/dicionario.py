traducoes = {
    "inglês": "spicy",
    "espanhol": "picante",
    "português": "picante",
    "francês": "épicé", 
    "japonês": "辛い" #karai

}

idioma = input("Digite o idioma: ").lower()
if idioma in traducoes:
    print(traducoes[idioma])

else:
    print("idioma não encontrado")