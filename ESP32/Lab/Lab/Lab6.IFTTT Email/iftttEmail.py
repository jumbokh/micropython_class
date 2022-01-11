from machine import Pin
import utime, urequests
from urlencode import urlencode
import xtools
import config
from dhtfun import getTemp

xtools.connect_wifi_led()
pIn4 = Pin(4, Pin.IN, Pin.PULL_UP)
button = 1 #Pin(4, Pin.IN, Pin.PULL_UP)
APIKEY = config.KEY
WEBHOOK_URL="https://maker.ifttt.com/trigger/ButtonClick/with/key/"
WEBHOOK_URL+=APIKEY + "?" 

print("請按下按鍵開關來送出Email…")
cnt=0
while True:
    button = pIn4.value()
    if button == 0:   # 值 0 是按下
        cnt += 1
        [T,H] = getTemp()    
        print("{0:4.2f} 度, {1:4.2f} %, #{2:2d}".format(T,H,cnt))
        params = { "value1": T,
                   "value2": H,
                   "value3": cnt}
        WEBHOOK_SEND = WEBHOOK_URL + urlencode(params)
        print("送出Email!")
        print(WEBHOOK_SEND)
        urequests.get(WEBHOOK_SEND)
        utime.sleep(10)
        print("Press....")
