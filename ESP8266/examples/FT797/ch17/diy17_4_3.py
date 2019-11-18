# -*- coding: utf-8 -*-

"""
   程式說明請參閱17-25頁
"""

from machine import Pin, Timer
import urequests as req
import dht
import time

d = dht.DHT11(Pin(2))
running = True

apiURL='{url}?key={key}'.format(
    url = 'http://api.thingspeak.com/update',
    key = '你的Write API KEY',
)

def sendDHT11(t):
    global apiURL, running

    try:
        d.measure()
    except OSError as e:
        print(e)
        return

    apiURL+='&field1={temp}&field2={humid}'.format(
        temp = d.temperature(),
        humid = d.humidity()
    )

    r = req.get(apiURL)

    if r.status_code != 200:
        t.deinit()
        print('Bad request error.')
        running = False
    else:
        print('Data saved, id: ', r.text)

tim = Timer(-1)
tim.init(period=20000, mode=Timer.PERIODIC, callback=sendDHT11)

try:
    while running:
        pass
except:
    tim.deinit()
    print('stopped')