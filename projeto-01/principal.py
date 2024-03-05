# 287*2 = 574 clicks necessários para SUBs
import pyautogui as py
import time as t

link_ole = "https://ola.oleconsignado.com.br"

py.press('win')
py.write('chrome')
py.press('enter')
t.sleep(1)
py.write(link_ole, interval=0.1)
py.press('enter')
t.sleep(2)
py.click(x=698, y=440, clicks=2)