# -*- coding: utf-8 -*-

"""
   程式說明請參閱11-10頁
"""

from machine import ADC, Pin
import time

ledPin = Pin(2, Pin.OUT)
adc = ADC(0)

while True:
    val = adc.read()

    if val >= 700:
        ledPin.value(0)
    else:
        ledPin.value(1)

    time.sleep(0.5)
