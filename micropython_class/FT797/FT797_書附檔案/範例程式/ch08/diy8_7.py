# -*- coding: utf-8 -*-

"""
   程式說明請參閱8-36頁
"""

import machine, neopixel
import time

np = neopixel.NeoPixel(machine.Pin(4), 8)

colors = ((100, 255, 255), (170, 235, 145), (235, 210, 35),
          (255, 150, 0), (255, 80, 0), (255, 0, 0), 
          (255, 40, 0),(255, 80, 0), (225, 120, 5), 
          (160, 170, 20), (100, 210, 45), (100, 235, 150))

lastColor = len(colors) - 1
ledTotal = 8
start = 0

try:
    while True:
        index = start

        for i in range(ledTotal):
            if index > lastColor:
                index = 0

            np[i] = colors[index]
            index = index + 1
        
        np.write()
        
        start = start + 1
        if start > lastColor:
            start = 0
        
        time.sleep_ms(50)
except:
    np.fill((0, 0, 0))
    np.write()
