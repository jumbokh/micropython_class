'''
測試連接麵包板上的LED燈
其 pin 腳為 D2 (4)
'''
from machine import Pin
import time

p2 = Pin(4, Pin.OUT)

for i in range(3):
    p2.value(0)
    time.sleep(1)
    p2.value(1)
    time.sleep(1)
p2.value(0)
