# -*- coding: utf-8 -*-

"""
   程式說明請參閱8-7頁
"""

from machine import Timer

tim1 = Timer(-1)
tim1.init(period=1000,mode=Timer.PERIODIC, callback=lambda t:print('Go, '))

tim2 = Timer(-1)
tim2.init(period=2000,mode=Timer.PERIODIC, callback=lambda t:print('Python!'))

try:
   while True:
     pass
except:
   tim1.deinit()
   tim2.deinit()
   print('stopped!')