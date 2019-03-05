# -*- coding: utf-8 -*-

"""
   程式說明請參閱10-7頁
"""

from machine import PWM, Pin
servo = PWM(Pin(0), freq=50)

period = 20000
minDuty = int(500/period * 1024)
maxDuty = int(2400/period * 1024)
unit = (maxDuty - minDuty)/180

def rotate(servo, degree=90):
   _duty = round(unit * degree) + minDuty
   _duty = min(maxDuty, max(minDuty, _duty))
   servo.duty(_duty)

rotate(servo, 60)
rotate(servo, 120)