#Criar uma função que ela vai printar uma mensagem padrão de saudação
#Ela vai saber o nome da pessoa como parâmetro
#SE o usuário não passar um argumento quando chamar a função, ela deve imprimir o nome padrão de 'Élton'

def saudacao(nome = 'Élton'):
    saudacao = f'bom dia, {nome}'
    return saudacao




x = saudacao('Caio')
print(x)

