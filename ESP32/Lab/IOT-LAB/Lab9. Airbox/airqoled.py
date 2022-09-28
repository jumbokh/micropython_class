import machine, dht, utime,ssd1306
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

def getDust():
    t,tot,t1=0,0,0
    ppm=0.0
    t1=measure()
    #print('Test measure Value :  ',t1,'---- this value always too low')
    for i in range(10):  # on fait 10 mesures
       t=measure()
       #print(i,"---",t)
       tot=tot+t
    ppm=tot/10
    return ppm

d11=dht.DHT11(machine.Pin(15))
hw_i2c1 = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))# machine.I2C(0x3c, freq=200000)        
oled096=ssd1306.SSD1306_I2C(128, 64, hw_i2c1)
oled096.fill(0) 
oled096.text('~ TEMP & HUMID ~',0,0)
oled096.text('Temp =    C',0,16)
oled096.text('Humid=    %',0,32)
oled096.text('PM2.5=     um',0,48)
oled096.show()
try:
    while 1:
        utime.sleep_ms(2000)
        d11.measure()
        oled096.fill(0)     
        oled096.text('~ TEMP & HUMID ~',0,0) 
        oled096.text('Temp = {} C'.format(d11.temperature()),0,16)
        oled096.text('Humid= {} %'.format(d11.humidity()),0,32)
        oled096.text('PM2.5=  {}um'.format(getDust()),0,48)
        oled096.show()
        print('today temp ={}, humidity= {}, PM2.5= {}'.format(d11.temperature(),d11.humidity(),getDust()))
except Exception as e: print(e)