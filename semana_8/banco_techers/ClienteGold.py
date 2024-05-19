from Cliente import Cliente

class ClienteGold(Cliente):
    def __init__(self, nome:str, cpf:str, contra_corrente:str, ativo:bool = True, saldo:float = 0, cheque_especial: float = 0, pre_credito = 0 ):
        super().__init__(nome, cpf, contra_corrente, ativo, cheque_especial, pre_credito)
        self.cheque_especial = 4000
        self.pre_credito = 4000

