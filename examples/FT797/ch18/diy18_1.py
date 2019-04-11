# -*- coding: utf-8 -*-

"""
   程式說明請參閱18-7頁
"""

import urequests as req
import ujson

apiURL='{url}?q={city}&APPID={key}'.format(
url = 'http://api.openweathermap.org/data/2.5/weather',
city = 'Taipei,TW',
key = '你的API Key'
)

r = req.get(apiURL)
obj = ujson.loads(r.text)

del r