from Veiculo import Veiculo
from Carro import Carro
from CarroEletrico import CarroEletrico
from Moto import Moto

tesla = CarroEletrico('Tesla', 'Model S', 2021)
uno = Carro('Fiat', 'Uno', 2021)
tesla.ligar()
tesla.encher_tanque()
uno.encher_tanque()

cg = Moto('Honda', 'CG 160', 2021)
cg.ligar()
cg.empinar()


cg.buzinar() #implementar depois