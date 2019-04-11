from machine import UART
com = UART(0, 9600)
com.init(9600)

gpsStr = b''        # 存放GPS資料的位元組陣列
gpsReading = False  # 是否繼續讀取，預設「否」。

def utcTime(timeStr):
    if timeStr == '':
        return ''
    
    hr = timeStr[0:2]
    min = timeStr[2:4]
    sec = timeStr[4:6]
    
    # 傳回「時時:分分:秒秒」格式字串
    return hr + ':' + min +':' + sec

def utcDate(dateStr):
    if dateStr == '':
        return ''

    day = dateStr[0:2]
    month = dateStr[2:4]
    year = dateStr[4:6]

    # 傳回「年年年年/月月/日日」格式字串
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

    lat = latitude(gps[3], gps[4])   # 緯度、北（N）或南（S）
    long = longitude(gps[5], gps[6]) # 經度、東（E）或西（W）
    today = utcDate(gps[9])  # 日期
    now = utcTime(gps[1])    # 時間

    return (lat, long, today, now)

def displayGPS(lat, long, today, now):
    lat = 'Lat: ' + lat    # 緯度值前面加上'Lat: '
    long = 'Long: ' + long # 經度值前面加上'Long: '

    print(today + '\n' + now + '\n' + lat + '\n' + long)


try:
    while True:
        data = com.readline()

        if data and (gpsReading or ('$GPRMC' in data)) :
            gpsStr += data    # 把符合的資料存入gpsStr變數

            if '\n' in data:  # 若資料包含'\n'…
                gpsReading = False  # …停止讀取並開始整理資料。
                lat, long, today, now = convertGPS(gpsStr)
                displayGPS(lat, long, today, now)  # 顯示解析後的GPS資料
                gpsStr = b''  # 清空GPS原始資料
            else:     # 若資料不含'\n'…就繼續讀取…
                gpsReading = True   # …設定成「繼續讀取」
                print("Keep reading...")
except:
    print("stopped.")