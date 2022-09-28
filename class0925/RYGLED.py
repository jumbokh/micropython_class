from machine import Pin
import time

p15 = Pin(15, Pin.OUT)
p2 = Pin(4, Pin.OUT)
p4 = Pin(16, Pin.OUT)

while True:
    # 開綠燈 5 秒
    p15.value(1)
    time.sleep(3)
    # 關綠燈，並開黃燈 1 秒
    p15.value(0)
    p2.value(1)
    time.sleep(2)
    # 關黃燈，並開紅燈 3 秒
    p2.value(0)
    p4.value(1)
    time.sleep(3)
    # 關紅燈
    p4.value(0)