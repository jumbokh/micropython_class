# -*- coding: utf-8 -*-

"""
   程式說明請參閱7-10頁
"""

from machine import Pin
import dht
import time

d = dht.DHT11(Pin(2))

def readDHT():
    d.measure()
    temp = d.temperature()
    t = str(temp) if temp > 9 else '0' + str(temp)
    humid = d.humidity()
    h = str(humid) if humid > 9 else '0' + str(humid)
    return (t+'\u00b0C', h+'%')

while True:
    (temp, humid) = readDHT()
    print('Temp: ' + temp)
    print('Humid: ' + humid)
    time.sleep(5)
