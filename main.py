from xml.dom import HierarchyRequestErr
import pyautogui
import time

pyautogui.alert('It will be started in 3ms after you click ok button')

time.sleep(3)

text = 'Hello Every All'

while True:
    pyautogui.typewrite(text)
    time.sleep(5)
    pyautogui.press('enter')
