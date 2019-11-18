# -*- coding: utf-8 -*-

"""
   程式說明請參閱4-8頁
"""

from machine import Pin

led = Pin(2, Pin.OUT)
sw = Pin(0, Pin.IN)

while True:
    val = sw.value()
    led.value(val)
