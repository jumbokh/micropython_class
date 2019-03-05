# -*- coding: utf-8 -*-

"""
   程式說明請參閱5-10頁
"""

from machine import Pin
import time
import MINI

led = Pin(MINI.D4, Pin.OUT)
MINI.hello()

while True:
    led.value(0)
    time.sleep(0.5)
    led.value(1)
    time.sleep(0.5)
