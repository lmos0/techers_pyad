
class Cliente:
    def __init__(self, nome, cpf, cnh):
        self.nome = nome
        self.cpf = cpf
        self.cnh = cnh
        self.carro_alugado = None
    
    # def alugar_carro(self, carro):
    #     self.carro_alugado = carro
    #     carro.disponibilidade = False
    # def devolver_carro(self):
    #     self.carro_alugado.disponibilidade = True
    #     self.carro_alugado = None