# 287*2 = 574 clicks necessários para SUBs
import pyautogui as py
import time as t
import datetime

link_ole = "https://ola.oleconsignado.com.br"
data_atual = datetime.date.today()
data_anterior = data_atual - datetime.timedelta(days=30)

py.press('win')
t.sleep(1)
py.write('chrome')
py.press('enter')
t.sleep(1)
py.write(link_ole, interval=0.01)
py.press('enter')
t.sleep(2)
py.press('tab')
py.write('LIDIANGFT38620')
py.press('tab')
py.write('Gftcredmais@27')
py.press('tab')
py.press('enter')
t.sleep(8)
py.click(x=1119, y=336)
py.click(x=1003, y=132)
py.click(x=297, y=219)
py.click(x=347, y=261)
py.click(x=182, y=597)
py.click(x=347, y=261)