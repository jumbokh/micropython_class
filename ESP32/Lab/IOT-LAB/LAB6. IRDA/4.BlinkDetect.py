#測試 4 : 指定 PIR 觸發後 LED 閃爍時間

from machine import Pin
import time
p0=Pin(33, Pin.IN)
p2=Pin(17, Pin.OUT)
duration=8                           #LED 持續閃爍之秒數

def LED_blink():
    p2.value(1)
    time.sleep_ms(50)
    p2.value(0)
    time.sleep_ms(50)

while True:
    if p0.value()==1:              #偵測到觸發訊號
        expire=duration*1000 + time.ticks_ms()    #計算結束時戳 (duration 換算成 ms)
        while time.ticks_ms() <= expire:            #若還未到達結束時戳就持續閃爍
            LED_blink()