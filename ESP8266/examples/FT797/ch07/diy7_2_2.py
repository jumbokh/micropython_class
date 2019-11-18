# -*- coding: utf-8 -*-

"""
   程式說明請參閱7-23頁
"""

from machine import UART
com = UART(0, 9600)
com.init(9600)

gpsStr = b''
gpsReading = False

while True:
    data = com.readline()

    if data and (gpsReading or ('$GPRMC' in data)) :
        gpsStr += data

        if '\n' in data:
            gpsReading = False
            lat, long, today, now = convertGPS(gpsStr)
            displayGPS(lat, long, today, now)
            gpsStr = b''
         else:
            gpsReading = True
            print("Keep reading...")
