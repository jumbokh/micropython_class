# -*- coding: utf-8 -*-

"""
   程式說明請參閱3-12頁
"""

from machine import Pin
import time
p2 = Pin(2, Pin.OUT)

while True:
    p2.value(0)
    time.sleep(0.5)
    p2.value(1)
    time.sleep(0.5)
