#the purpose of this program is to automatically research 30 numbers in Microsoft Edge in order to earn points for Microsoft Rewards
#version:: 1.0
#You can install the pyautogui library by typing "py -m pip install pyautogui" in the command prompt
#created by Matteo Maiullari
import pyautogui as pag
import time

print("Close this window to end the program execution")
print("It is reccomended not to interact with the PC during the execution")

time.sleep(3)

pag.press('win')
time.sleep(1)
pag.write('edge')
pag.press('enter')

time.sleep(2)

pag.hotkey('ctrl', 'l')

pag.write('1')
pag.press('enter')
time.sleep(7)

for i in range (2,31):
    pag.hotkey('ctrl', 'l')
    pag.write(str(i))
    pag.press('space')
    pag.press('enter')
    time.sleep(7)
