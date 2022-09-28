from machine import Pin
import utime

button = 4
led = 2

pIn4 = Pin(4, Pin.IN, Pin.PULL_UP)

pOutled = Pin(led, Pin.OUT)


button = 1 #Pin(4, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)
while True:
  button = pIn4.value()
  print(button)
  pOutled.value(button)
  utime.sleep(1)
