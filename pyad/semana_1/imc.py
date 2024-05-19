# weight (kg) / (height (m) * height (m))

peso = float(input('Digite o seu peso em kilogramas '))
altura = float(input('Digite sua altura em metros '))

imc = peso / (altura ** 2)

print('O seu IMC é ', imc)

if imc < 18.5:
    print('abaixo do peso ideal')
elif imc >= 18.5 and imc <= 25.0:
    print('seu peso está normal')

elif imc >= 25.0 and imc <= 30.0:
    print('você está com sobrepeso')

else:
    print('grau de obesidade')

"texto literal" = str 
23 = int
23.8 = float 
False = bool
True  = bool 

if 
elif -> checa uma condicional ATÉ se encontrar um condicional verdadeira

AND e OR 

print()
input()
int()
str()
float()

cor = "vermelho"
cor.