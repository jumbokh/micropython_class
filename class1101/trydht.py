import machine, dht

d11=dht.DHT11(machine.Pin(15))
d11.measure()                    # start to measure
t=d11.temperature()        # return the temperature
h=d11.humidity()        # return the humidity
print("{0:4.2f} 度, {1:4.2f} %".format(t,h))