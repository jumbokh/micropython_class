# -*- coding: utf-8 -*-

"""
   程式說明請參閱8-4頁
"""

from machine import Pin, Timer
LED = Pin(13, Pin.OUT)

def blink(t):
    LED.value(not LED.value())

tim = Timer(-1)
tim.init(period=500, mode=Timer.PERIODIC, callback=blink)

try:
   while True:
     pass
except KeyboardInterrupt:
   tim.deinit()
   print('stopped!')
