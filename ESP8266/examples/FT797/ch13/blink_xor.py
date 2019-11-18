# -*- coding: utf-8 -*-

"""
   程式說明請參閱13-42頁
"""

from machine import Pin
import time

led = Pin(2, Pin.OUT)

while 1:
    led.value(led.value() ^ 1)
    time.sleep(0.5)
