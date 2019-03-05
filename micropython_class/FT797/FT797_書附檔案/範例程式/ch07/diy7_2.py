# -*- coding: utf-8 -*-

"""
   程式說明請參閱7-21頁
"""

from machine import UART
com = UART(0, 9600)
com.init(9600)

while True:
    data = com.readline()
    if data:
        print(data)
