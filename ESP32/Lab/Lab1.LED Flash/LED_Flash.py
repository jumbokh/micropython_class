from machine import Pin
import utime

LED = None


LED = Pin(13, Pin.OUT)
while True:
  LED.value(0)
  utime.sleep(1)
  LED.value(1)
  utime.sleep(1)