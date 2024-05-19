from Cliente import Cliente
from ClienteGold import ClienteGold
from ClienteSilver import ClienteSilver 

luis = Cliente('Luis', '123.456.789-00', '1234-5', True)
luis.info()
luis.deposito(300)
luis.consultar_saldo()

elton = ClienteSilver('Elton', '987.654.321-00', '5432-1', True)
elton.deposito(433)
elton.saque(2000)
elton.info()

joao = ClienteGold('João', '123.456.789-10', '2234-5', True)
joao.deposito(1000)
joao.info()