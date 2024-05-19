import pyautogui
import time

print(pyautogui.size())
time.sleep(3)
print(pyautogui.position())

pyautogui.moveTo(6,88, duration=2)
time.sleep(2)
pyautogui.doubleClick(6,88,button='left')
time.sleep(1)
pyautogui.hotkey('ctrl','c')
time.sleep(0.6)
pyautogui.press('down')
time.sleep(0.6)
pyautogui.press('enter')
time.sleep(0.6)
pyautogui.hotkey('ctrl', 'v')

# pyautogui.moveTo(850,650, duration=2)
# pyautogui.moveRel(0,-50, duration=2)

# pyautogui.click(100,0,button="left")
# pyautogui.rightClick(100,100, duration=1.5)

# pyautogui.hotkey('ctrl','c')
# time.sleep(1)
# pyautogui.press('down')
# time.sleep(1)
# pyautogui.press('enter')
# time.sleep(1)
# pyautogui.hotkey('ctrl', 'v')

# pyautogui.scroll(200)