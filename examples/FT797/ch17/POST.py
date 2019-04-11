# -*- coding: utf-8 -*-

"""
   程式說明請參閱17-28頁
"""

import urequests as req

apiURL='http://api.thingspeak.com/update'
payload='key={key}&field1={temp}&field2={humid}'.format(
    key='你的Write API_KEY',
    temp=21,
    humid=47
)

r=req.post(apiURL, data=payload)
print(r.text)