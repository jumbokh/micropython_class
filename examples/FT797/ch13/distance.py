# -*- coding: utf-8 -*-

"""
   程式說明請參閱13-11頁
"""

from hcsr04 import HCSR04
import time

sr04 = HCSR04()

try:
    while True:
        try:
            print('Distance:', sr04.distance(), 'cm')
        except Exception:
            print(Exception.args[0])
        
        time.sleep(1)

except KeyboardInterrupt:
    print('Program stopped.')