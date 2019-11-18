# -*- coding: utf-8 -*-

"""
   程式說明請參閱15-15頁
"""

from machine import Pin, SPI

cs = Pin(15, Pin.OUT)
spi = SPI(1)

DECODEMODE = const(9)
INTENSITY = const(10)
SCANLIMIT = const(11)
SHUTDOWN = const(12)
DISPLAYTEST = const(15)

symbol = (0x60, 0xF0, 0xF0, 0x7F, 0x07, 0x06, 0x0C, 0x08)

def max7219(reg, data):
    cs.value(0)
    spi.write(bytes([reg, data]))
    cs.value(1)

def init():
    max7219(DISPLAYTEST, 0)
    max7219(SCANLIMIT, 7)
    max7219(INTENSITY, 8)
    max7219(DECODEMODE, 0)
    max7219(SHUTDOWN, 1)

'''
def init():
    for reg, data in (
        (DISPLAYTEST, 0),
        (SCANLIMIT, 7),
        (INTENSITY, 8),
        (DECODEMODE, 0),
        (SHUTDOWN, 1)
    ):
        max7219(reg, data)
'''

def show():
    for i in range(8):
        max7219(i + 1, symbol[i])

init()
show()