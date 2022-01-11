import machine, dht
import utime, urequests
from urlencode import urlencode
import xtools
import config

def getTemp(pin=15):
    d11=dht.DHT11(machine.Pin(pin))
    d11.measure()                    # start to measure
    utime.sleep(1)
    t=d11.temperature()        # return the temperature
    h=d11.humidity()        # return the humidity
    return [t,h]

xtools.connect_wifi_led()
APIKEY = config.TAPIKEY
WEBHOOK_URL="https://api.thingspeak.com/update?api_key="
WEBHOOK_URL+=APIKEY + "&field1=" 

input("請按下按鍵開關來送出Data…")

[T,H] = getTemp()    
print("{0:4.2f} 度, {1:4.2f} %, #{2:2d}".format(T,H,1))
params = { "value1": T,
           "value2": H,
           "value3": 1}
WEBHOOK_SEND = WEBHOOK_URL + str(T) + "&field2=" + str(H)
print("送出 ThingSpeak!")
print(WEBHOOK_SEND)
urequests.get(WEBHOOK_SEND)


