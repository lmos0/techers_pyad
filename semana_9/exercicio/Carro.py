class Carro:
    def __init__(self, modelo, ano, cor, disponibilidade=True):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.disponibilidade = disponibilidade
    
    def __str__(self):
        return f'Modelo: {self.modelo}, Ano: {self.ano}, Cor:{self.cor}, Disponibilidade:{self.disponibilidade}'


# mobi = Carro('Mobi', 2023, 'branca')
# byd = Carro('Dolphin', 2024, 'preta', False)
# print(mobi)
# print(byd)