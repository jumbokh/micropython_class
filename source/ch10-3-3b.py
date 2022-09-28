from machine import Pin
import utime, xtools
from urlencode import urlencode
import config

xtools.connect_wifi_led()
button = Pin(4, Pin.IN, Pin.PULL_UP)

API_KEY = config.KEY
value1 = 100
value2 = "陳會安"
params = { "value1": value1,
           "value2": value2 }
WEBHOOK_URL="https://maker.ifttt.com/trigger/ButtonClick/with/key/" + API_KEY
WEBHOOK_URL+="/?" + urlencode(params)

print("請按下按鍵開關來送出Email…")
while True:
    if button.value() == 0:   # 值 0 是按下
        xtools.webhook_get(WEBHOOK_URL)
        utime.sleep(10)