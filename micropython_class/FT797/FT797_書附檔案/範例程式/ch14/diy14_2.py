# -*- coding: utf-8 -*-

"""
   程式說明請參閱14-21頁
"""

from machine import Pin

led = Pin(2, Pin.OUT, value=1)
sw = Pin(0, Pin.IN, Pin.PULL_UP)

def callback(p):
    global led
    led.value(not led.value())

sw.irq(trigger=Pin.IRQ_RISING, handler=callback)