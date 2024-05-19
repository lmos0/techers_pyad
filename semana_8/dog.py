#Programação Orientada a Objetos
# Programar de forma a representar um objeto real. Algo que existe no mundo

# atributos = adjetivos (caractéristica)
# métodos = verbos (ações)
class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print(f'{self.nome} diz: Au Au!')
    
    def cocar(self):
        print(f'{self.nome} ** está se coçando **')

cachorro1 = Cachorro("Salaminho", "Salsicha")
cachorro2 = Cachorro('Mostarda', 'Poodle')

cachorro1.latir()
cachorro1.cocar()

cachorro2.cocar()




