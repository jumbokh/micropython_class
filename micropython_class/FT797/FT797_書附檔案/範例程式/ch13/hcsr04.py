# -*- coding: utf-8 -*-

"""
   程式說明請參閱13-9頁
"""

from machine import Pin
import machine, time

class HCSR04:
    def __init__(self, trigPin=16, echoPin=14):
        self.echoTimeout = 23200
        self.trigPin = Pin(trigPin, mode=Pin.OUT)
        self.echoPin = Pin(echoPin, mode=Pin.IN)
        self.trigPin.value(0)

    def distance(self):
        self.trigPin.value(1)
        time.sleep_us(10)
        self.trigPin.value(0)

        pulseTime = machine.time_pulse_us(self.echoPin, 1, self.echoTimeout)

        if pulseTime > 0:
            return pulseTime / 58
        else:
            raise Exception('Out of the detection range.')
