from machine import Pin
import machine, dht
import utime, urequests
from urlencode import urlencode
import xtools
import config

xtools.connect_wifi_led()

led = 2
d11=dht.DHT11(machine.Pin(15))
pIn4 = Pin(4, Pin.IN, Pin.PULL_UP)

pOutled = Pin(led, Pin.OUT)
APIKEY = config.KEY
WEBHOOK_URL="https://maker.ifttt.com/trigger/ButtonClick/with/key/"
WEBHOOK_URL+=APIKEY + "?" 

button = 1 #Pin(4, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)
print("請按下按鍵開關來送出Email…")
cnt=0
while True:
    
  d11.measure()                    # start to measure
  button = pIn4.value()
  #print(button)
  pOutled.value(button)
  if button == 0:   # 值 0 是按下
        cnt += 1
        T=d11.temperature()        # return the temperature
        H=d11.humidity()        # return the humidity
        print("{0:4.2f} 度, {1:4.2f} %, {2:2d}".format(T,H,cnt))
        params = { "value1": T,
                   "value2": H,
                   "value3": cnt}
        WEBHOOK_SEND = WEBHOOK_URL + urlencode(params)
        print("送出Email!")
        print(WEBHOOK_SEND)
        print(".",end="")
        utime.sleep(10)