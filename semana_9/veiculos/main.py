from Carro import Carro
from Veiculo import Veiculo
from CarroEletrico import CarroEletrico
from Moto import Moto


gol = Carro('vw', 'gol', 1998)
tesla = CarroEletrico('Tesla', 'Model S', 2020)
biz = Moto('Honda', 'Biz', 2003)

tesla.encher_tanque()
tesla.checar_bateria()

gol.encher_tanque()

biz.empinar()

biz.buzinar()
tesla.buzinar()


