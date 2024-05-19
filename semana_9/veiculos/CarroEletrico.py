from Carro import Carro

class CarroEletrico(Carro):
    def __init__(self,marca,modelo,ano_de_fabricacao):
        super().__init__(marca,modelo,ano_de_fabricacao)
        self.bateria = 70

    def checar_bateria(self):
        print(f'Este carro está com {self.bateria}% de bateria!')

    def encher_tanque(self):
        print('Este não carro não precisa encher o tanque')