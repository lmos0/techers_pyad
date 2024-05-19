class Filial:
    def __init__(self,nome):
        self.nome = nome
        self.carros = []

    def add_carro(self,carro):
        self.carros.append(carro)

    def emprestar_carro(self, modelo, cliente):
        for carro in self.carros:
            if carro.modelo == modelo:
                carro.disponibilidade = False
                return carro, None
        return None, None
    def receber_carro(self, modelo):
        for carro in self.carros:
            if carro.modelo == modelo:
                carro.disponibilidade = True
                return carro
        return None
    def verificar_carros(self):
        print("Lista de carros:")
        for carro in self.carros:
            print(carro)  # Use __str__ method of Carro class
        print("-----")