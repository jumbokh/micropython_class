# -*- coding: utf-8 -*-

"""
   程式說明請參閱8-33頁
"""

import machine, neopixel

np = neopixel.NeoPixel(machine.Pin(4), 8)

np[0] = (0, 1, 0) 
np[2] = (127, 45, 127)
np[4] = (255, 127, 40)

np.write()