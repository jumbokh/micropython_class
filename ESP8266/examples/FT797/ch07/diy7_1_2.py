# -*- coding: utf-8 -*-

"""
   程式說明請參閱7-11頁
"""

from machine import Pin
import dht
import time

d = dht.DHT11(Pin(2))

def readDHT():
    d.measure()
    t = '{:02}\u00b0C'.format(d.temperature())
    h = '{:02}%'.format(d.humidity())
    return (t, h)

while True:
    (temp, humid) = readDHT()
    print('Temp: ' + temp)
    print('Humid: ' + humid)
    time.sleep(5)
