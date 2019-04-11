# -*- coding: utf-8 -*-

"""
   程式說明請參閱4-17頁
"""

import time
from machine import Pin

led = Pin(2, Pin.OUT)
sw = Pin(0, Pin.IN)

while True:
    if sw.value() == 0 :
        time.sleep_ms(20)
        led.value(not led.value())
        while sw.value() == 0 :
            pass
