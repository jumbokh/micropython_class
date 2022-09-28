from machine import Pin
import machine, dht
import utime

button = 4
led = 2
d11=dht.DHT11(machine.Pin(15))
pIn4 = Pin(4, Pin.IN, Pin.PULL_UP)

pOutled = Pin(led, Pin.OUT)


button = 1 #Pin(4, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)
while True:
  d11.measure()                    # start to measure
  button = pIn4.value()
  print(button)
  pOutled.value(button)
  t=d11.temperature()        # return the temperature
  h=d11.humidity()        # return the humidity
  print("{0:4.2f} 度, {1:4.2f} %".format(t,h))
  utime.sleep(3)
