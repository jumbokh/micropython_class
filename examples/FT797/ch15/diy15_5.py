# -*- coding: utf-8 -*-

"""
   程式說明請參閱15-24頁
"""

from machine import Pin, SPI
import os
import sdcard

sd = sdcard.SDCard(SPI(1), Pin(15))
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')

with open('/sd/test.txt', 'a') as f:
    f.write('hello\r\nworld\r\n')