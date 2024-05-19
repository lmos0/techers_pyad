from Carro import Carro
from Cliente import Cliente
from Filial import Filial

# Registrar Carros
abc123 = Carro("HB20", 2020, "Preto")
abc321 = Carro("City", 2019, "Branco")

#Registrar Filial
loja1 = Filial("Loja 1")
loja1.verificar_carros()

#Registrar Cliente
carlos = Cliente("Carlos", "123.456.789-00", "12345678900")
renan = Cliente("Renan", "987.654.321-00", "98765432100")

#Vincular carro à filial
loja1.add_carro(abc123)
loja1.add_carro(abc321)

#Verificar carros disponíveis
loja1.verificar_carros()
loja1.emprestar_carro("City", carlos)   
loja1.emprestar_carro("HB20", renan)
loja1.verificar_carros()
loja1.receber_carro("City")
loja1.verificar_carros()

