from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.tanque = 20

    def empinar(self):
        print("A moto está empinando!")