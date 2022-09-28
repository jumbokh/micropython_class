# ADC : 34
# ILED : GIPO16
#=====================================================================
from machine import Pin, ADC
import time
p0 = Pin(13, Pin.OUT)
adc = ADC(Pin(35))
def measure():
 p0.value(1)                       # d?but du cr?neau
 time.sleep_us(280)         # les 0.28 ms
 readvalue = adc.read()    # lecture de l’adc
 time.sleep_us(40)           # compl?ment du cr?neau ? 0.32 ms
 p0.value(0)                        # fin du cr?neau
 time.sleep_us(9680)        # compl?ment du cycle ? 10 ms
 return readvalue
#--------------------------------------
t=measure()
def getDust():
  t,tot,t1=0,0,0
  ppm=0.0
  for i in range(10):  # on fait 10 mesures
     t=measure()
     tot=tot+t
  ppm=tot/10
  return ppm

while True:
    p = getDust()
    print(p)
    time.sleep(0.5)