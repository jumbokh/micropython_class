# -*- coding: utf-8 -*-

"""
   程式說明請參閱10-16頁
"""

from machine import Pin
from servo import Servo
import time

swPin = Pin(0, Pin.IN)
s = Servo(15)
s.rotate(90)

while True:
    if not swPin.value():
        s.rotate(150)
        time.sleep(2)
        s.rotate(90)
        time.sleep(1)
