#Programação Orientada a Objetos
# Programar de forma a representar um objeto real. Algo que existe no mundo

# atributos = adjetivos (caractéristica)
# métodos = verbos (ações)
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

class ClienteSilver(Cliente):
    def __init__(self, nome:str, cpf:str, conta_corrente:str, ativo:bool = True, saldo:float = 0,cheque_especial:float = 0, pre_credito:float = 0) -> None:
        super().__init__(nome, cpf, conta_corrente, ativo, cheque_especial, pre_credito)
        self.cheque_especial = 1000
        self.pre_credito = 1000


pamela = ClienteSilver('Pâmela', '322.122.111-32', '4343-2', True)
pamela.deposito(300)
pamela.info()

# elton = Cliente('Élton', '123.456.654-32', '4040-8')
# caio = Cliente('Caio', '321.421.333-22', '4035-8')
# joao = Cliente('João', '458.222.112-23', '3340-8')
# luis = Cliente('Luís', '123.345.432-12', '3322-9' )


# elton.deposito(400.00)
# elton.saque(300)
# elton.info()

# luis.saque(150)


