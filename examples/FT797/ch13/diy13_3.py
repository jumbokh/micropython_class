from machine import I2C, Pin
from hcsr04 import HCSR04
import wemotor
import time

dir = 0             # 記錄行進狀態，0代表「前進」，1代表「右轉」。
limitDist = 10      # 距離上限10公分
sr04 = HCSR04()     # 建立超音波物件

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
motorA = wemotor.Motor(wemotor.A, i2c)    # 建立馬達A物件
motorB = wemotor.Motor(wemotor.B, i2c)    # 建立馬達B物件

def stop():         # 停止
    motorA.setMotor(wemotor.STOP)
    motorB.setMotor(wemotor.STOP)

def forward():      # 前進
    motorA.setMotor(wemotor.CW)
    motorB.setMotor(wemotor.CW)

def turnRight():    # 右轉
    motorA.setMotor(wemotor.CW)
    motorB.setMotor(wemotor.CCW)

while True:
    try:
        dist = sr04.distance()  # 讀取距離值
    except Exception:
        dist = 400              # 若超過檢測範圍，則預設為400公分。

    if dist > limitDist:        # 若距離超過10公分
        if dir != 0:            # 若目前不是「前進」狀態
           stop()               # 先停止馬達0.5秒
           dir = 0
           time.sleep(0.5)

        forward()   # 前進
    else:                       # 若距離小於10公分
        if dir != 1:            # 若目前不是「右轉」狀態
           stop()               # 先停止馬達0.5秒
           dir = 1
           time.sleep(0.5)
           
        turnRight() # 右轉
        
    time.sleep(1)