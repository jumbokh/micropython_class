from machine import Pin
import time

p2 = Pin(15, Pin.OUT)

for i in range(3):
    p2.value(0)
    time.sleep(1)
    p2.value(1)
    time.sleep(1)
