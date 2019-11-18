# -*- coding: utf-8 -*-

"""
   程式說明請參閱8-5頁
"""

from machine import Pin, Timer
LED = Pin(13, Pin.OUT)

tim = Timer(-1)
tim.init(period=500, mode=Timer.PERIODIC, callback=lambda t: LED.value(not LED.value()))

try:
   while True:
     pass
except:
   tim.deinit()
   LED.value(0)
   print('stopped!')