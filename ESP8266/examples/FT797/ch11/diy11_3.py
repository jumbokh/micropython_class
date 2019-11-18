# -*- coding: utf-8 -*-

"""
   程式說明請參閱11-17頁
"""

import machine
adc = machine.ADC(0)

def temp(adc, R0=10000.0, T0=25.0, beta=3950.0):
    import math

    r = (adc * R0) / (1023 - adc)
    T0 += 273.15
    return 1/(1/T0 + 1/beta*math.log(r/R0))-273.15

val = adc.read()
t = temp(val)
print("temp: ", str(t))
