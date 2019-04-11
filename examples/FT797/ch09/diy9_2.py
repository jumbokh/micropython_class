# -*- coding: utf-8 -*-

"""
   程式說明請參閱9-11頁
"""

from machine import Pin, PWM
import time

swPin = Pin(0, Pin.IN)
buzzer = PWM(Pin(14))

print('Start!')

try:
    while True:
        if swPin.value() == 0:
            buzzer.duty(900)
            buzzer.freq(500)
            time.sleep(1.5)
            buzzer.duty(0)
except:
    buzzer.deinit()
    print('Game Over')
