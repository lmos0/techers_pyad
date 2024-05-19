class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


    def __str__(self):
        return f'{self.marca} {self.modelo} {self.ano}'
    
    def ligar(self):
        print('O veículo está ligado.')
    
    def desligar(self):
        print('O veículo está desligado.')
    
    def buzinar(self):
        print('beep beep')

    