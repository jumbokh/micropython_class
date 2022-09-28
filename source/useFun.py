from dhtfun import getTemp

while True:
    [t,h] = getTemp()    
    print("{0:4.2f} 度, {1:4.2f} %".format(t,h))
    utime.sleep(2)