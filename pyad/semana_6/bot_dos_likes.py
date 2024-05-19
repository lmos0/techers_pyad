import pyautogui
import time

print(pyautogui.size())
time.sleep(2)
print(pyautogui.position())

for i in range(5):
    pyautogui.move(773,260, duration=2)
    time.sleep(1.5)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.moveRel(-250,0, duration=1.5)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1.2)
    pyautogui.press('right')
