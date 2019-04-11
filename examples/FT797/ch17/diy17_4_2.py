# -*- coding: utf-8 -*-

"""
   程式說明請參閱17-24頁
"""

import urequests as req

apiURL='{url}?key={key}&field1={temp}&field2={humid}'.format(
    url   = 'http://api.thingspeak.com/update',
    key   = '你的Write API KEY',
    temp  = 22,
    humid = 25
)

r = req.get(apiURL)

if r.status_code != 200:
    print('Bad request')
else:
    print('Data saved, id: ', r.text)