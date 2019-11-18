# -*- coding: utf-8 -*-

"""
   程式說明請參閱14-23頁
"""

from machine import UART
from machine import Pin, I2C
import time
import ssd1306
import os

led = Pin(2, Pin.OUT, value=1)
sw = Pin(0, Pin.IN, Pin.PULL_UP)

file = None
saveFile = False
filePath = '/gps.csv'

interval = 5000
saveTime = time.ticks_ms()

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text("GPS RUNNING...", 0, 30)
oled.show()

def callback(p):
    global saveFile, led, saveTime

    val = p.value()
    if val == 1:
        saveTime = 0
        led.value(not led.value())
        saveFile = not saveFile

sw.irq(trigger=Pin.IRQ_RISING, handler=callback)

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

def saveGPS(lat, long, today, now):
    global file, saveFile, filePath

    if saveFile:
        if file == None:
            try:
                os.stat(filePath)
                file = open(filePath, 'a')
            except OSError as e:
                if (e.args[0] == 2):
                    file = open(filePath, 'a')
                    file.write('latitude,longitude,date,time\r\n')

        file.write(lat +','+ long + ',' + today + ',' + now + '\r\n')
    else:
        if file != None:
            file.close()
            print('file closed.')
            file = None

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
    global saveTime
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

                if time.ticks_diff(time.ticks_ms(), saveTime) > interval:
                    saveGPS(lat, long, today, now)
                    saveTime = time.ticks_ms()

                gpsStr = b''
            else:
                gpsReading = True

main()