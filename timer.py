import time
import random

def sleep(t):
    time.sleep(t + (random.random() - 0.5)*t/2)