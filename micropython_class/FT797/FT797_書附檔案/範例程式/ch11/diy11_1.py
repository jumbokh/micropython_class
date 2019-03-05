# -*- coding: utf-8 -*-

"""
   程式說明請參閱11-4頁
"""

from machine import Pin, PWM, ADC
import time

adc = ADC(0)
ledPin = Pin(2, Pin.OUT)
LED = PWM(ledPin,1000)

while True:
    val = adc.read()
    LED.duty(val)
    print('POT: ', str(val))
    time.sleep(0.5)
