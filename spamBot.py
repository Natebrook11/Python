from asyncio.windows_events import INFINITE
from ctypes.wintypes import PUSHORT
import pyautogui 
import time

spam_text=input("Spam text:")

time.sleep(5)

for x in range(40):
    pyautogui.write(spam_text , interval=0.01)
    pyautogui.press("enter")

print("Spam done!") 