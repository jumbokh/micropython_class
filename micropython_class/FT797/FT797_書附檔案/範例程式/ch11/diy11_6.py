# -*- coding: utf-8 -*-

"""
   程式說明請參閱11-28頁
"""

from machine import ADC
from machine import Pin
import time

led = Pin(2, Pin.OUT)
adc = ADC(0)

claps = 0
lastTime = 0

while True:
    val = adc.read()

    if val > 350:
        claps += 1
        print('claps: ' + claps)

        if claps == 2:
            timeDiff = time.ticks_diff(time.ticks_ms(), lastTime) 
            print('timeDiff: ' + str(timeDiff))
            
            if timeDiff > 500 and timeDiff < 1500:
                claps = 0
                led.value(not led.value())
            else:
                claps = 1
        
        lastTime = time.ticks_ms()
        time.sleep(0.4)
