#Crie uma classe Livro com os atributos: titulo, autor, editora e numero_paginas. 

#Implemente um método resumir() que imprime as informações básicas do livro

#atributos -> características do objeto (adjetivos)
#métodos -> ações daquele objeto (verbo) 
    #métodos são funções, mas quando funções estão no escopo de um objeto elas são chamadas de Métodos
#__ -> dunder
class Livro:
    def __init__(self, titulo, autor, editora, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.numero_paginas = numero_paginas
    
    def resumir(self):
        print(f'Título : {self.titulo}')
        print(f'Título : {self.autor}')
        print(f'Editora: {self.editora}')
        print(f'Número de Páginas: {self.numero_paginas}') 


livro1 = Livro('A Revolução dos Bichos', 'George Orwell', 'Companhia das Letras', 128)
livro2 = Livro('O Senhor dos Anéis: A Sociedade do Anel', "J.R.R. Tolkien", 'Martins Fontes', 504)
livro1.resumir()
livro2.resumir()
