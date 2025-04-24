from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
import random


def key_press(symbol):
    keyboard.press(symbol)
    keyboard.release(symbol)


def printer(text):
    for i in text:
        key_press(i)
        time.sleep(random.random()/2)

