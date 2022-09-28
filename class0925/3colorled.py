from machine import Pin, PWM
from time import sleep
import clist

frequency = 5000
red = PWM(Pin(15), frequency)
green = PWM(Pin(2), frequency)
blue = PWM(Pin(4), frequency)
#clist = [[255,255,0],[0,255,255],[255,0,255],[104,42,67],[102,98,133]]

while True:
    for x in clist.hlist:
        red.duty(x[0])
        green.duty(x[1])
        blue.duty(x[2])
        sleep(1)
    