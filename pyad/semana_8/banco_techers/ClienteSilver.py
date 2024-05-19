from Cliente import Cliente

class ClienteSilver(Cliente):
    def __init__(self, nome:str, cpf:str, conta_corrente:str, ativo:bool = True, saldo:float = 0,cheque_especial:float = 0, pre_credito:float = 0) -> None:
        super().__init__(nome, cpf, conta_corrente, ativo, cheque_especial, pre_credito)
        self.cheque_especial = 1000
        self.pre_credito = 1000