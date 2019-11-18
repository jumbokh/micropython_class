# -*- coding: utf-8 -*-

"""
   程式說明請參閱15-18頁
"""

from machine import Pin, SPI
import time

DECODEMODE = const(9)
INTENSITY = const(10) #0xA
SCANLIMIT = const(11) #0xB
SHUTDOWN = const(12)  #0xC
DISPLAYTEST = const(15) #0xF

sprite = ( 
    (0x30, 0x7c, 0xae, 0x3e, 0x3e, 0xae, 0x7c, 0x30),
    (0x18, 0xbe, 0x57, 0x1f, 0x1f, 0x57, 0xbe, 0x18),
    (0x30, 0xbc, 0x6e, 0x3e, 0x3e, 0x6e, 0xbc, 0x30),
    (0x18, 0x9e, 0x57, 0xbf, 0xbf, 0x57, 0x9e, 0x18)
)

cs = Pin(15, Pin.OUT)
spi = SPI(1)

def max7219(reg, data):
    cs.value(0)
    spi.write(bytes([reg, data]))
    cs.value(1)

def init():
    for reg, data in (
        (DISPLAYTEST, 0),
        (SCANLIMIT, 7),
        (INTENSITY, 8),
        (DECODEMODE, 0),
        (SHUTDOWN, 1)
    ):
        max7219(reg, data)

def clear():
    for i in range(8):
        max7219(i + 1, 0)

def animate():
    for i in range(4):
        for j in range(8):
            max7219(j+1, sprite[i][j])
        time.sleep(0.3)

try:
    init()
    while True:
        animate()  
except:
    clear()