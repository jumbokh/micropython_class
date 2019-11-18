# -*- coding: utf-8 -*-

"""
   程式說明請參閱8-25頁
"""

from machine import Pin

CLK = Pin(14, Pin.IN)
DT =  Pin(12, Pin.IN)
counter = 0
prev = CLK.value()

while True:
    now = CLK.value()

    if now != prev:
        if DT.value() != now:
            counter += 1
        else: 
            counter -= 1
        
        print("counter: " + str(counter))

    prev = now
