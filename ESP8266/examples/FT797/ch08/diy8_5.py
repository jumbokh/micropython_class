# -*- coding: utf-8 -*-

"""
   程式說明請參閱8-28頁
"""

from machine import Pin
import color

R_PIN = PWM(Pin(2))
G_PIN = PWM(Pin(0))
B_PIN = PWM(Pin(4))

CLK = Pin(14, Pin.IN)
DT =  Pin(12, Pin.IN)
prev = CLK.value()
counter = 0
step = 2.5

while True:
    now = CLK.value()

    if now != prev:
        if DT.value() != now:
            counter = (counter + step) % 360
        else:
            counter = (counter - step) % 360

        print("counter: " + str(counter))

        RGB = color.hsv2rgb(counter, 1, 1)
        R_PIN.duty(RGB[0])
        G_PIN.duty(RGB[1])
        B_PIN.duty(RGB[2])

    prev = now
