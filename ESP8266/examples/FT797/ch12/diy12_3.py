# -*- coding: utf-8 -*-

"""
   程式說明請參閱12-21頁
"""

import ssd1306
from machine import I2C, Pin

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.text('No Hack,', 0, 0)
oled.text('No Life!', 50, 30)

oled.show()

oled.invert(True)
oled.invert(False)
oled.fill(0)
oled.show()