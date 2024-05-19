from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.tanque = 50

    def encher_tanque(self):
        print("O tanque está cheio!")

    def descricao_tanque(self):
        print(f"Este carro tem um tanque de {self.tanque} litros.")

