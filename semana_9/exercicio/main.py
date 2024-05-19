#Locadora de carros

#Precisar de uma classe Carro -> Na qual eu vou informar características  (modelo, cor, ano)
 # modelo, ano, cor, disponibilidade (True ou False)

#Precisar de uma classe Cliente -> Registrar informações de diferentes diferentes (nome, cpf,cnh)
# nome, cpf, cnh e está_com_carro (True ou False)

# Criar classe Filial na qual será possível organizar os veículos disponiveis
# nome, carros disponíveis (será uma lista)
# emprestar carro, receber carro e vericar os carros disponiveis
#############################################################################################
from Cliente import Cliente
from Carro import Carro
from Filial import Filial

#Loja foi instanciada (palavra bonita para criação de um novo objeto tipo loja)
loja_01 = Filial('Loja 1')
loja_02 = Filial('Loja 02')
print(loja_01, loja_02)


#Usamos o métodos do tipo Loja, Verificar Carro
loja_01.verificar_carro()

#Carros instanciados (palavra bonita pra criamos um novo objeto do tipo Carro)
abc_123 = Carro('Mobi', 2023, 'branca')
abc_456 = Carro('Dolphin', 2024, 'preta', False)
abc_789 = Carro('Duster', 2023, 'prata')
abc_099 = Carro('Kwid', 2022, 'vermelha')

#Usamos o método tipo Loja, adicionar carro
loja_01.add_carro(abc_123)



loja_01.verificar_carro()

#Clientes

elton = Cliente('Élton', "123.456.789-00", "33355599")

loja_01.emprestar_carro('Mobi')

loja_01.verificar_carro()




