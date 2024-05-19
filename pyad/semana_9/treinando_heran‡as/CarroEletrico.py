from Carro import Carro

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.bateria = 70

    def descricao_bateria(self):
        print(f"Este carro tem uma bateria de {self.bateria}-kWh.")

    def encher_tanque(self):
        print("Este carro não precisa de tanque!")