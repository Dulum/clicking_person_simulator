import os
import time
import random

def sleep(t):
    noise = (random.gauss(0,t/4)) ** 2
    noise = noise ** .5
    time.sleep(t + noise)

def presskey(key, repeat=1, wait=0.3):
    for _ in range(repeat):
        os.system("xdotool key " + key)
        sleep(wait)
        
def nav_html(ls):
    for x in ls:
        presskey("Down", repeat=x)
        presskey("Right")        

sleep(5)
presskey("F5", wait=3)
presskey("Page_Down", repeat=4, wait=1)
sleep(3)
presskey("F12", wait=8)
nav_html([2, 3, 1, 1, 2, 2, 2, 2, 3])
presskey("Menu", wait=1)
presskey("Down", repeat=5)
presskey("Right")
presskey("Return")