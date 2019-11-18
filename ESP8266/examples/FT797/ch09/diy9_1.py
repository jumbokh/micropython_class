# -*- coding: utf-8 -*-

"""
   程式說明請參閱9-9頁
"""

from machine import Pin, PWM
import time

buzzer = PWM(Pin(14, Pin.OUT), duty=900)

def sndEffect(): 
    buzzer.freq(400)
    time.sleep(0.5)
    buzzer.freq(700)
    time.sleep(0.5)

for i in range(5):
    sndEffect()

buzzer.deinit()
