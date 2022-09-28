#測試 1 : 偵測到移動使 LED 閃爍  
from machine import Pin
import time
p0=Pin(33, Pin.IN)          #接 PIR 感測器信號輸出 (中間腳)
p2=Pin(17, Pin.OUT)      #接 LED + 220 歐姆電阻

def LED_blink():           #閃爍 LED 一次的函數
    p2.value(1)
    time.sleep_ms(50)     #暫停 50 ms
    p2.value(0)
    time.sleep_ms(50)      #暫停 50 ms

while True:
    if p0.value()==1:       #PIR 偵測到人體移動時輸出 High (3.3V)
        LED_blink()          #讓 LED 閃爍
    else:                           #移動停止時 PIR 輸出 Low
        p2.value(0)            #讓 LED 熄滅