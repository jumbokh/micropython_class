# -*- coding: utf-8 -*-

"""
   程式說明請參閱17-7頁
"""

from machine import Pin
import dht, socket

d = dht.DHT11(Pin(2))

s = socket.socket()
HOST = '0.0.0.0'
PORT = 80

httpHeader = b"""\
HTTP/1.0 200 OK

<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>ESP8266 Webserver</title>
</head>
<body>
  Temperture: {temp}<br>
  Humid: {humid}
</body>
</html>
"""

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)
print("Web server is running.")

def readDHT():
    d.measure()
    t = '{:02}\u00b0C'.format(d.temperature())
    h = '{:02}%'.format(d.humidity())
    return (t, h)

while True:
    client, _ = s.accept()
    temp, humid = readDHT()
    client.send(httpHeader.format(temp, humid))
    client.close()