#測試 2 : 計算 PIR 輸出 High 的時間長度
from machine import Pin
import time
p0=Pin(33, Pin.IN)
p2=Pin(17, Pin.OUT)
waitForLow=False                                     #狀態旗標:用來計算輸出 High 的時間
timerStart=time.ticks_ms()                       #紀錄 High 時長的計時器

def LED_blink():                                        #閃爍 LED 一次的函數
    p2.value(1)
    time.sleep_ms(50)                                  #暫停 50 ms
    p2.value(0)
    time.sleep_ms(50)                                  #暫停 50 ms

while True:
    if p0.value()==1:                                     #PIR 偵測到人體移動時輸出 High (3.3V)
        if not waitForLow:                              #目前是 Low 狀態
            timerStart=time.ticks_ms()            #取得目前時戳更新計時器開始計時
            waitForLow=True                           #更新狀態旗標 : 等待 Low 到來
        LED_blink()
    else:                                                         #PIR 輸出 Low
        if waitForLow:                                    #原先狀態為 High
            print(time.ticks_ms()-timerStart)    #計算時長
            waitForLow=False                           #狀態旗標歸零
        p2.value(0)                                           #熄滅 LED