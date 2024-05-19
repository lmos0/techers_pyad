class Aeronave:
    # método construtor recebe um parâmetro (self) e não retorna nada. Self representa a própria instância da classe.
    def __init__(self, fabricante:str, modelo:str, capacidade:int):
        self.fabricante = fabricante
        self.modelo = modelo
        self.capacidade = capacidade

    # método que retorna uma string com as informações da aeronave
    def info (self):
        print( f'{self.fabricante} {self.modelo} - {self.capacidade} passageiros')
    
    # método que retorna a capacidade da aeronave
    def get_capacidade(self):
        return self.capacidade

pt_azl = Aeronave('Embraer', 'E195', 124)
pt_brf = Aeronave('ATR', 'atr-72', 72)

pt_azl.info()
pt_brf.info()