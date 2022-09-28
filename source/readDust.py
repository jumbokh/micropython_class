# ADC : A0
# ILED : D3 / GIPO00
#=====================================================================
from machine import Pin, ADC
import time
p0 = Pin(16, Pin.OUT)
adc = ADC(Pin(34))
def measure():
 p0.value(1)                       # d?but du cr?neau
 time.sleep_us(280)         # les 0.28 ms
 readvalue = adc.read()    # lecture de l’adc
 time.sleep_us(40)           # compl?ment du cr?neau ? 0.32 ms
 p0.value(0)                        # fin du cr?neau
 time.sleep_us(9680)        # compl?ment du cycle ? 10 ms
 return readvalue
#--------------------------------------
print('PM2.5 Result:')
t,tot,t1=0,0,0
ppm=0.0
t1=measure()
print('Test measure Value :  ',t1,'---- this value always too low')
for i in range(10):  # on fait 10 mesures
 t=measure()
 print(i,"---",t)
 tot=tot+t
ppm=tot/10
tot2='PM2.5 Value = '+str(ppm)[:5]
print(tot2)
print('Finish.....')