from machine import Pin
import utime, urequests
from urlencode import urlencode
import xtools
import config

xtools.connect_wifi_led()
button = Pin(4, Pin.IN, Pin.PULL_UP)

APIKEY = config.KEY
value1 = 100
value2 = "陳會安"
params = { "value1": value1,
           "value2": value2 }
WEBHOOK_URL="https://maker.ifttt.com/trigger/ButtonClick/with/key/"
WEBHOOK_URL+=APIKEY + "/?" + urlencode(params)

print("請按下按鍵開關來送出Email…")
while True:
    if button.value() == 0:   # 值 0 是按下
        print("送出Email!")
        urequests.get(WEBHOOK_URL)
        utime.sleep(10)