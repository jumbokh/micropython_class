# -*- coding: utf-8 -*-

"""
   程式說明請參閱5-4頁
"""

from machine import Pin
import time
p2 = Pin(2, Pin.OUT)

def blink():
    for i in range(5):
        p2.value(0)
        time.sleep(0.5)
        p2.value(1)
        time.sleep(0.5)
