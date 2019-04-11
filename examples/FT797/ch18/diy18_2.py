# -*- coding: utf-8 -*-

"""
   程式說明請參閱18-11頁
"""

from machine import Pin, I2C, Timer
import bigSymbol
import ssd1306
import framebuf
import os
import urequests as req
import ujson

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

apiURL='{url}?q={city}&APPID={key}'.format(
    url = 'http://api.openweathermap.org/data/2.5/weather',
    city = '城市名稱',
    key = '你的API _KEY'
)

def checkIcon(n):
    path = '/icons/'+ n
    try:
        os.stat(path)
        return path
    except:
        return '/icons/na.bin'

def update(t=None):
    r = req.get(apiURL)
    obj = ujson.loads(r.text)

    city = obj['name']
    icon = obj['weather'][0]['icon']
    temp = int(obj['main']['temp'] - 273.15)
    humid = obj['main']['humidity']

    path = checkIcon(icon + '.bin')
    f = open(path, 'rb')
    buf = f.read()
    f.close()

    oled.fill(0)
    fb = framebuf.FrameBuffer(bytearray(buf), 48, 48, framebuf.MVLSB)
    oled.text(city, 0, 0)
    oled.framebuf.blit(fb, 0, 15)

    dsp = bigSymbol.Symbol(oled)
    dsp.text(str(temp) + 'c', 60, 20)
    dsp.text(str(humid) + '%', 60, 45)
    oled.show()

tim = Timer(-1)
tim.init(period=600000, mode=Timer.PERIODIC, callback=update)
update()

try:
    while True:
        pass
except:
    tim.deinit()
    print('stopped!')