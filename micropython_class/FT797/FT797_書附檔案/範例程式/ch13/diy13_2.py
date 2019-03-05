from hcsr04 import HCSR04
from machine import Pin, PWM, Signal
import time

sr04 = HCSR04()
ledPin = PWM(Pin(2), freq=1000)  # led接在第2腳
led = Signal(ledPin, invert=True)

def setPWM(dist, pin):  # 依據輸入距離，調整輸出PWM。
    dist = max(minDist, min(dist, maxDist))  # 數值限縮在最低與最高限度之間
    pwm = (dist-minDist) / (maxDist - minDist) * 1024
    pin.duty(pwm);    # 控制指定腳位的PWM輸出

while True:
    try:
        dist = sr04.distance()
            print('Distance:', dist, 'cm')

        if dist < limitDist:  # 若距離在指定範圍內，才需要調整亮度。
            setPWM(dist, led)

    except Exception as e
        print(e.args[0])
    
    time.sleep(1)