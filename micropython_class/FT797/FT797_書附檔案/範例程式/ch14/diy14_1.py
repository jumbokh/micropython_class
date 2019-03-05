# -*- coding: utf-8 -*-

"""
   程式說明請參閱14-5頁
"""

from machine import UART
from machine import Pin, I2C
import time
import ssd1306
import os

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text("GPS RUNNING...", 0, 30)
oled.show()

def utcDateTime(dateStr, timeStr, timeZone=8):
    if dateStr == '' or timeStr == '':
        return None

    day = dateStr[0:2]
    month = dateStr[2:4]
    year = dateStr[4:6]
    hr = timeStr[0:2]
    min = timeStr[2:4]
    sec = timeStr[4:6]
    timeZone *= 3600

    t = time.mktime((int('20' + year), int(month), int(day),int(hr), int(min), int(sec), 0, 0))

    return time.localtime(t+timeZone)

def latitude(d, h):
    if d == '':
        return '0'

    hemi = '' if h == 'N' else '-'
    deg = int(d[0:2])
    min = str(float(d[2:]) / 60)[1:]

    return hemi + str(deg) + min

def longitude(d, h):
    if d == '':
        return '0'

    hemi = '' if h == 'E' else '-'
    deg = int(d[0:3])
    min = str(float(d[3:]) / 60)[1:]

    return hemi + str(deg) + min

def convertGPS(gpsStr):
    gps = gpsStr.split(b'\r\n')[0].decode('ascii').split(',')

    lat = latitude(gps[3], gps[4])  # N or S
    long = longitude(gps[5], gps[6]) # E or W
    today = ''
    now = ''
    tim = utcDateTime(gps[9], gps[1], 8)

    if tim != None:
        today = str(tim[0]) + '/' + str(tim[1]) + '/' + str(tim[2])
        now = str(tim[3]) + ':' + str(tim[4]) + ':' + str(tim[5])

    return (lat, long, today, now)

def displayGPS(lat, long, today, now):
    lat = "Lat: " + lat
    long = "Long: " + long
    oled.fill(0)
    oled.text(today, 0, 0)
    oled.text(now, 0, 10)
    oled.text(lat, 0, 20)
    oled.text(long, 0, 30)
    oled.show()

def main():
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

main()