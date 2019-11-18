# -*- coding: utf-8 -*-

"""
   程式說明請參閱17-23頁
"""

import urequests as req

apiURL='{url}?key={key}&field1={temp}&field2={humid}'.format(
    url   = 'http://api.thingspeak.com/update',
    key   = '你的Write API KEY',
    temp  = 22,
    humid = 25
)

r = req.get(apiURL)

print('content:', r.content)
print('text:', r.text)