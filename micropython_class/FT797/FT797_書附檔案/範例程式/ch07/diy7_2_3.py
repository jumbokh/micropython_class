# -*- coding: utf-8 -*-

"""
   程式說明請參閱7-24頁
"""

from machine import UART
com = UART(0, 9600)
com.init(9600)

gpsStr = b''
gpsReading = False

def utcTime(timeStr):
    if timeStr == '':
        return ''
    
    hr = timeStr[0:2]
    min = timeStr[2:4]
    sec = timeStr[4:6]

    return hr + ':' + min +':' + sec

def utcDate(dateStr):
    if dateStr == '':
        return ''

    day = dateStr[0:2]
    month = dateStr[2:4]
    year = dateStr[4:6]

    return '20' + year + '/' + month +'/' + day

def latitude(d, h):
    if d == '':
        return '0'

    hemi = '' if h == 'N' else '-'
    deg = d[0:2]
    min = str(float(d[2:])/60)[1:]

    return hemi + deg + min

def longitude(d, h):
    if d == '':
        return '0'

    hemi = '' if h == 'E' else '-'
    deg = d[0:3]
    min = str(float(d[3:])/60)[1:]

    return hemi + deg + min

def convertGPS(gpsStr):
    gps = gpsStr.split(b'\r\n')[0].decode('ascii').split(',')

    lat = latitude(gps[3], gps[4])
    long = longitude(gps[5], gps[6])
    today = utcDate(gps[9])
    now = utcTime(gps[1])

    return (lat, long, today, now)

def displayGPS(lat, long, today, now):
    lat = 'Lat: ' + lat
    long = 'Long: ' + long

    print(today + '\n' + now + '\n' + lat + '\n' + long)

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
