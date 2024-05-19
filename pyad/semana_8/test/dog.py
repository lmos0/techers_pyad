class Cachorro:
  def __init__(self, nome, raça):
    self.nome = nome
    self.raca = raça

cachorro = Cachorro("Rex", "Pitbull")

# Acessando o atributo nome do objeto cachorro
nome_cachorro = cachorro.raca

print(f"O nome do cachorro é {nome_cachorro}")  # Saída: O nome do cachorro é Rex
