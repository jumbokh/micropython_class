from machine import Pin
import time

irda = Pin(17, Pin.IN, Pin.PULL_UP)

p16 = Pin(16, Pin.OUT)


button = 1 #Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    button = irda.value()
    #print(sr501)
    if button == 1:
        p16.value(1)
        utime.sleep(1)
    else:
        p16.value(0)