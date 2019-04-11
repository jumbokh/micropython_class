# -*- coding: utf-8 -*-

"""
   程式說明請參閱11-26頁
"""

from machine import ADC
from machine import Pin
import time

led = Pin(2, Pin.OUT)
adc = ADC(0)

while True:
    val = adc.read()

    if val > 120:
        led.value(not led.value())
        print(val)