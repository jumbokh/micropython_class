# -*- coding: utf-8 -*-

"""
   程式說明請參閱4-17頁
"""

from machine import Pin

toggle = 1

led = Pin(2, Pin.OUT)
sw = Pin(0, Pin.IN)

while True:
    if sw.value() == 0 :
        toggle = not toggle
        led.value(toggle)
