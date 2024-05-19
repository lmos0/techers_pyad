import pyautogui
import time

# 201 337
# while True:
#     print(pyautogui.position())

time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.click(201, 337, 1000, 0.05, button='left')