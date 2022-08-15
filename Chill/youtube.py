import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

# Para colocar uma música no youtube
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyperclip.copy("https://www.youtube.com/")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")
time.sleep(7)
pyautogui.click(x=688, y=132)
pyautogui.write("sex memories chris brown")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=1016, y=459)
