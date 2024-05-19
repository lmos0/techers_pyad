
class Filial:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []
    
    def add_carro(self,carro):
        self.carros.append(carro)
        print('Carro adicionado ao estoque com sucesso')
    
    def emprestar_carro(self, modelo):
        for c in self.carros:
            if c.modelo == modelo:
                c.disponibilidade = False
                return c 
        return None
    
    def receber_carro(self, modelo):
        for c in self.carros:
            if c.modelo == modelo:
                c.disponibilidade(True)
                return c
        return None
    
    def verificar_carro(self):
        print('Lista de Carros:')
        for c in self.carros:
            print(c)
        print('--------')

    def __str__(self) -> str:
        return f'A unidade {self.nome} foi criada!'



