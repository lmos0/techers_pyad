class Cliente:
    def __init__(self, nome:str, cpf:str, conta_corrente:str, ativo:bool = True, saldo:float = 0, cheque_especial = 0, pre_credito = 0 ):
        self.nome = nome
        self.cpf = cpf
        self.conta_corrente = conta_corrente
        self.ativo = ativo
        self.saldo = saldo
        self.cheque_especial = 0
        self.credito = 0
        self.pre_credito = pre_credito
    
    def info(self):
        print(f'Nome: {self.nome} - CPF: {self.cpf} - Conta Corrente {self.conta_corrente} - Ativo: {self.ativo} - Saldo: {self.saldo}')
    
    def deposito(self, valor:float):
        self.saldo += valor
        print(f'Depósito de R$ {valor} foi realizado com sucesso. Saldo atual: R$ {self.saldo}')
    
    def saque(self, valor:float):
        if self.saldo + self.cheque_especial >= valor:
            self.saldo -= valor
            print(f'Saque de R$ {valor} realizado com sucesso. Saldo atual: R$ {self.saldo}')
        else:
            print('Saldo Insuficiente')