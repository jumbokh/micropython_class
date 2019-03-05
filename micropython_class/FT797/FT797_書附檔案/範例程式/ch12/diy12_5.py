# -*- coding: utf-8 -*-

"""
   程式說明請參閱12-33頁
"""

import bigSymbol
from machine import Pin, I2C
import ssd1306
import dht
import time

d = dht.DHT11(Pin(13))
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
dsp = bigSymbol.Symbol(oled)
dsp.clear()
dsp.temp(0, 18)
dsp.humid(0, 38)

interval = 3000

def readDHT():
    d.measure()
    temp = d.temperature()
    t = '{:02}c'.format(temp)
    humid = d.humidity()
    h = '{:02}%'.format(humid)
    return (t, h)

def main():
    lastTime = interval
    
    while True:
        delta = time.ticks_diff(time.ticks_ms(), lastTime)

        if delta >= 0:
            temp, humid = readDHT()
            dsp.text(temp, 34, 18)
            dsp.text(humid, 34, 38)
            oled.show()
            lastTime = time.ticks_ms() + interval

main()