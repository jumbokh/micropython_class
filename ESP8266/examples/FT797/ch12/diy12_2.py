# -*- coding: utf-8 -*-

"""
   程式說明請參閱12-17頁
"""

from machine import Pin, I2C
from servo import Servo
import time

servoX = Servo(12)
servoY = Servo(14)
scale = 0.71

PCF8591 = 0x48
VRX = '\x02'
VRY = '\x03'

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

while True:
    i2c.writeto(PCF8591, VRX)
    i2c.readfrom(PCF8591, 1)
    data = i2c.readfrom(PCF8591, 1)
    servoX.rotate(data[0] * scale)

    i2c.writeto(PCF8591, VRY)
    i2c.readfrom(PCF8591, 1)
    data = i2c.readfrom(PCF8591, 1)
    servoY.rotate(data[0] * scale)