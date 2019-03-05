# -*- coding: utf-8 -*-

"""
   程式說明請參閱8-22頁
"""

from machine import Pin, PWM
import time
import color

R_PIN = PWM(Pin(2))
G_PIN = PWM(Pin(0))
B_PIN = PWM(Pin(4))

def wheel():
    for i in range(360):
        RGB = color.hsv2rgb(i, 1, 1)
        R_PIN.duty(RGB[0])
        G_PIN.duty(RGB[1])
        B_PIN.duty(RGB[2])
        time.sleep_ms(50)

wheel()