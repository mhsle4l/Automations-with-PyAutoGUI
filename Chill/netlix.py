import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("netflix")
pyautogui.press("enter")
time.sleep(6)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.write("barbie")
time.sleep(2)
pyautogui.click(x=244, y=246)
pyautogui.click(x=649, y=252)
