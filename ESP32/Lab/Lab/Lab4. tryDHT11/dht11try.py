import machine, dht
import utime

d11=dht.DHT11(machine.Pin(13))
while True:
    d11.measure()                    # start to measure
    temp=d11.temperature()        # return the temperature
    humid=d11.humidity()        # return the humidity
    print("%3d 度C, %3d %%"%(temp,humid))
    utime.sleep(3)