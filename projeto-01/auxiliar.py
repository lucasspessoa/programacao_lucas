import pyautogui
import time

time.sleep(5)
currentMouseX, currentMouseY = pyautogui.position()

print(currentMouseX)
print(currentMouseY)

# time.sleep(5)
# pyautogui.click(x=762, y=293, clicks=180)