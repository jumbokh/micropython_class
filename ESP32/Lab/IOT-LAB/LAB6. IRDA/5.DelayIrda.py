#測試 5 : PIR 持續觸發使 LED 延遲熄滅

from machine import Pin
import time
p0=Pin(33, Pin.IN)
p2=Pin(17, Pin.OUT)
state=0
triggerCount=0       #觸發次數紀錄器 (最高次數為 triggerLimit 所規範)
triggerLimit=5        #觸發次數紀錄器上限值
highDelay=10.0      #點亮 LED 之秒數

def int0(p):                         #中斷處理函數  (必須傳入一個參數 : IRQ 腳位)
    global state                    #取用全域變數
    global triggerCount       #取用全域變數
    global triggerLimit        #取用全域變數
    state=1                           #LED 點亮狀態
    if triggerCount < triggerLimit:        #觸發次數紀錄器低於上限就增量
        triggerCount=triggerCount + 1
    print(p,"IRQ Trigger Count:",triggerCount)

p0.irq(trigger=Pin.IRQ_RISING, handler=int0)     #設定 GPIO 0 為上升緣觸發 IRQ 中斷

while True:
    if state==1:                         #LED 點亮狀態
        p2.value(1)                     #點亮 LED
        time.sleep(highDelay)    #暫停秒數
        triggerCount=triggerCount - 1        #觸發紀錄器減量
        print("Trigger Count:", triggerCount)
        if triggerCount <= 0:                       #觸發紀錄器歸零時熄滅 LED
            state=0
    else:
        p2.value(0)                      #熄滅 LED