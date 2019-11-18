# -*- coding: utf-8 -*-

"""
   程式說明請參閱13-31頁
"""

import ustruct

A = const(0)   # Motor A
B = const(1)   # Motor B

BRAKE = const(0)
CCW = const(1)
CW = const(2)
STOP = const(3)
STANDBY = const(4)

class Motor:
    def __init__(self, motor, i2c, address=0x30, freq=1000, standbyPin=None):
        if motor==A:
            self.motor=A
        else:
            self.motor=B
            
        self.i2c = i2c
        self.address = address
        self.standbyPin = standbyPin

        if standbyPin is not None:
            standbyPin.init(standbyPin.OUT, 0)

        self.setFreq(freq)

    def setMotor(self, dir, speed):
        if self.standbyPin is not None:
            if dir == STANDBY:
                self.standbyPin.value(0)
                return
            else:
                self.standbyPin.value(1)

        _speed = speed * 100

        if _speed > 10000:
            _speed = 10000

        if dir not in range(0,5):
           dir = 3

        s0 = _speed >> 8 & 0xff
        s1 = _speed & 0xff

        self.i2c.writeto(self.address, ustruct.pack(">4B", self.motor | 0x10, dir, s0, s1))
        
    def setFreq(self, freq):
        n0 = freq >> 16 & 0x0f
        n1 = freq >> 16 & 0xff
        n2 = freq & 0xffff

        self.i2c.writeto(self.address, ustruct.pack(">2BH", n0, n1, n2))