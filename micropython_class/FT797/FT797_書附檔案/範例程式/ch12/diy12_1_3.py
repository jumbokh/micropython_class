# -*- coding: utf-8 -*-

"""
   程式說明請參閱12-14頁
"""

from machine import Pin, I2C
import time

PCF8591 = 0x48
CH0 = b'\x00'
CH1 = b'\x01'
CH2 = b'\x02'

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

while True:
    i2c.writeto(PCF8591, CH0)
    i2c.readfrom(PCF8591, 1)
    data = i2c.readfrom(PCF8591, 1)
    print('THM: ' + str((data[0])))
    
    i2c.writeto(PCF8591, CH1)
    i2c.readfrom(PCF8591, 1)
    data = i2c.readfrom(PCF8591, 1)
    print('LDR: ' + str((data[0])))

    i2c.writeto(PCF8591, CH2)
    i2c.readfrom(PCF8591, 1)
    data = i2c.readfrom(PCF8591, 1)
    print('POT: ' + str((data[0])))
    time.sleep(5)
