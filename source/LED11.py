from machine import Pin
import utime

LED = None


LED = Pin(11, Pin.OUT)
while True:
  LED.value(0)
  utime.sleep(1)
  LED.value(1)
  utime.sleep(1)