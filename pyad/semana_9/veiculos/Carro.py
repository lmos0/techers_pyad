from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano_de_fabricacao):
        super().__init__(marca,modelo,ano_de_fabricacao)

    def encher_tanque(self):
        print('O tanque está cheio')

