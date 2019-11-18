# -*- coding: utf-8 -*-

"""
   程式說明請參閱3-24頁
"""

from machine import Pin, Signal
ledPin = Pin(2, Pin.OUT, value=1)
led = Signal(ledPin, invert=True)
led.value(1)
led.value(0)
led.on()
led.off()