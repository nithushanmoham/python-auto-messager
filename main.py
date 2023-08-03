from xml.dom import HierarchyRequestErr
import pyautogui
import time

pyautogui.alert('It will be started in 5ms after you click ok button')

time.sleep(5)

text = 'Hi'

while True:
    pyautogui.typewrite(text)
    time.sleep(2)
    pyautogui.press('enter')

