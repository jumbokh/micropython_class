# -*- coding: utf-8 -*-

"""
   程式說明請參閱13-7頁
"""

from machine import Pin
import machine, time

echoTimeout = 23200
trigPin = Pin(16, mode=Pin.OUT)
echoPin = Pin(14, mode=Pin.IN)
trigPin.value(0)

def distance():
    trigPin.value(1)
    time.sleep_us(10)
    trigPin.value(0)

    pulseTime = machine.time_pulse_us(echoPin, 1, echoTimeout)
    if pulseTime > 0:
        return pulseTime / 58
    else:
        return pulseTime

while True:
    cm = distance()
    if cm > 0:
        print('Distance:', cm, 'cm')
    else:
        print('Out of the detection range.')
        
        time.sleep(1)