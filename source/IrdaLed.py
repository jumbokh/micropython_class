#測試 3 : 指定 PIR 觸發後 LED 點亮時間

from machine import Pin
import time
p0=Pin(33, Pin.IN)
p2=Pin(17, Pin.OUT)
highDelay=4.5                       #LED 持續點亮之秒數

while True:
    if p0.value()==1:
        p2.value(1)                     #點亮 LED
        time.sleep(highDelay)    #持續點亮指定之秒數
        p2.value(0)                      #時間到熄滅 LED