# -*- coding: utf-8 -*-

"""
   程式說明請參閱7-22頁
"""

from machine import UART
com = UART(0, 9600)
com.init(9600)

while True:
    data = com.readline()
    if data and ('$GPRMC' in data):
        print(data)
