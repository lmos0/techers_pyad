from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano_de_fabricacao):
        super().__init__(marca,modelo, ano_de_fabricacao)
        # self.tanque = 20

    def empinar(self):
        print('A moto está empinando!')

        