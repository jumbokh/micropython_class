from machine import Pin
import time

p15 = Pin(15, Pin.OUT)
p2 = Pin(2, Pin.OUT)
p4 = Pin(4, Pin.OUT)

while True:
    p15.value(0)
    time.sleep(1)
    P15.value(1)
    time.sleep(1)
p15.value(0)