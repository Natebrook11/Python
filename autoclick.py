from logging.config import listen
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

mouse = Controller()

start_stop_key = KeyCode(char="q")

def on_press(key):
    if(key == start_stop_key):
        mouse.click(Button.left,100)

with Listener(on_press=on_press) as Listener:
    Listener.join()