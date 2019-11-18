# -*- coding: utf-8 -*-

"""
   程式說明請參閱12-13頁
"""

from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
i2c.writeto(0x48, '\x01')
i2c.readfrom(0x48, 1)
data = i2c.readfrom(0x48, 1)