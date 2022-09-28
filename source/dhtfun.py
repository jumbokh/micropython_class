import machine, dht
import utime

def getTemp(pin=15):
    d11=dht.DHT11(machine.Pin(pin))
    d11.measure()                    # start to measure
    utime.sleep(1)
    t=d11.temperature()        # return the temperature
    h=d11.humidity()        # return the humidity
    return [t,h]

while True:
    [t,h] = getTemp()    
    print("{0:4.2f} 度, {1:4.2f} %".format(t,h))
    utime.sleep(2)