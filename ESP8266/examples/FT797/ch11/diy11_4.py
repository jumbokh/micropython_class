# -*- coding: utf-8 -*-

"""
   程式說明請參閱11-20頁
"""

from target import Target
from machine import ADC, Pin
import time

adc = ADC(0)
servoPin = 0
score = 0

def setScore(id):
    global score
    score += 10
    print('shot servo', id)
    print('score:', score)

s1 = Target(servoPin)
s1.callback(setScore)
s1.start()

try:
    while True:
        val = adc.read()

        if val < 200:
            s1.shot()
except KeyboardInterrupt:
    s1.stop()
    print('Program stopped. Score:', score)
