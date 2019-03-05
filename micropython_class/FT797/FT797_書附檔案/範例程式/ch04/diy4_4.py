# -*- coding: utf-8 -*-

"""
   程式說明請參閱4-25頁
"""

from machine import Pin

led = Pin(2, Pin.OUT, value=1)
sw = Pin(5, Pin.IN)

while True:
    if sw.value() == 1 :
        led.value(not led.value())
        while sw.value() == 1 :
            pass
