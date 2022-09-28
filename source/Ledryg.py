from machine import Pin
import utime

#LEDR = None
#LEDY = None
#LEDG = None

LEDR = Pin(17, Pin.OUT)
LEDY = Pin(16, Pin.OUT)
LEDG = Pin(4, Pin.OUT)
while True:
  LEDR.value(1)
  utime.sleep(1)
  LEDR.value(0)
  utime.sleep(1)
  LEDY.value(1)
  utime.sleep(1)
  LEDY.value(0)
  utime.sleep(1)
  LEDG.value(1)
  utime.sleep(1)
  LEDG.value(0)
  utime.sleep(1)