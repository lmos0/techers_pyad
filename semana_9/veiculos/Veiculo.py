class Veiculo: 
    #método construtor. Ele define os atributos (as característica) de um objeto. E constrói o objeto por meio dos atributos
    
    #########Aqui foi definido os atributos do objeto
    def __init__ (self, marca, modelo, ano_de_fabricacao):
        self.marca = marca
        self.modelo = modelo
        self.ano_de_fabricacao = ano_de_fabricacao

    ########Aqui é definido os métodos(ações) do objeto
    
    #Essa função converte as informações do objeto em String, para facilitar leitura do usuário. Caso não isso não seja feito, apenas o endereço de memória será impresso
    def __str__(self):
        return f'O veículo é da marca {self.marca}, é de modelo {self.modelo}, e foi fabricado em {self.ano_de_fabricacao}'
    
    def ligar(self):
        print('O veículo está ligado')
    
    def desligar(self):
        print('O veículo está desligado')
    
    def buzinar(self):
        print('bip, bip')

