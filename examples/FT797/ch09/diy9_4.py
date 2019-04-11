# -*- coding: utf-8 -*-

"""
   程式說明請參閱9-22頁
"""

from machine import Pin, PWM

motorPin = Pin(13, Pin.OUT)
MOTOR = PWM(motorPin, 1000)
CLK = Pin(14, Pin.IN)
DT =  Pin(12, Pin.IN)
power = 0
step = 10
prev = CLK.value()

while True:
   now = CLK.value()

   if now != prev:
       if DT.value() != now:
          power = min(1023, power+step)
       else:
          power = max(0, power-step)
            
       print("power: " + str(power))
       MOTOR.duty(power)

   prev = now