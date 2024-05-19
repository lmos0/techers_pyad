import pyautogui
import time
import random

# print(pyautogui.size())

while True:
    largura_tela, altura_tela = pyautogui.size()
    x = random.randint(0, largura_tela)
    y = random.randint(0, largura_tela)

    pyautogui.moveTo(x,y, duration=0.75)

    intervalo = random.uniform(1,5)
    time.sleep(intervalo)