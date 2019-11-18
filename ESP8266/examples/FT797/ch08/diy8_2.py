# -*- coding: utf-8 -*-

"""
   程式說明請參閱8-13頁
"""

from machine import Pin,Timer,PWM

ledPin = Pin(13, Pin.OUT)
LED = PWM(ledPin,1000)
step = 32
_duty = 0
ms = round(1500 / step)

def breath(t):
    global _duty,step

    _duty += step

    if _duty > 1023:
        _duty = 1023
        step *= -1
    
    if _duty < 0:
        _duty = 0
        step *= -1

    LED.duty(_duty)

tim = Timer(-1)
tim.init(period=ms,mode=Timer.PERIODIC, callback=breath)

try:
   while True:
     pass
except:
   tim.deinit()
   LED.deinit()
   ledPin.value(0)
   print('stopped!')