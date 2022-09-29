from machine import Pin, PWM
from time import sleep
import random
import clist

frequency = 5000
red = PWM(Pin(15), frequency)
green = PWM(Pin(4), frequency)
blue = PWM(Pin(16), frequency)
#clist = [[255,255,0],[0,255,255],[255,0,255],[104,42,67],[102,98,133]]

while True:
    n =random.randint(0, 14)
    print(n)
    x = clist.clist[n]
    red.duty(x[0])
    green.duty(x[1])
    blue.duty(x[2])
    sleep(1)