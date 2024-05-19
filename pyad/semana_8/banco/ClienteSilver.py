from Cliente import Cliente

class ClienteSilver(Cliente):
    def __init__(self, nome:str, cpf:str, conta_corrente:str, ativo:bool, saldo:float = 0,cheque_especial:float = 0, pre_credito:float = 0) -> None:
        super().__init__(nome, cpf, conta_corrente, ativo, cheque_especial, pre_credito)
        self.cheque_especial = 1000
        self.pre_credito = 1000

    def info(self) -> None:
        print(f'Nome: {self.nome} - CPF: {self.cpf} - Conta Corrente: {self.conta_corrente} - Ativo: {self.ativo} - Saldo: {self.saldo} - Cheque Especial: {self.cheque_especial}, pré-crédito: {self.pre_credito}')
    def deposito(self, valor:float) -> None:
        self.saldo += valor
        print(f'Depósito de R$ {valor} realizado com sucesso. Saldo atual: R$ {self.saldo}')
    
    def saque(self, valor:float) -> None:
        if self.saldo + self.cheque_especial >= valor:
            self.saldo -= valor
            print(f'Saque de R$ {valor} realizado com sucesso. Saldo atual: R$ {self.saldo}')
        else:
            print('Saldo insuficiente.')
    def consultar_saldo(self) -> float:
        print(f'Saldo atual: R$ {self.saldo}')