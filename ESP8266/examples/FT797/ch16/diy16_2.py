# -*- coding: utf-8 -*-

"""
   程式說明請參閱16-26頁
"""

import socket

url = 'http://swf.com.tw/openData/test.html'
_, _, host, path = url.split('/', 3)

addr = socket.getaddrinfo(host, 80)[0][-1]
s = socket.socket()
s.connect(addr)

httpHeader = b'''\
GET /{path} HTTP/1.0
Host:{host}
User-Agent: MicroPython

'''

s.send(httpHeader.format(path=path, host=host))

while True:
    data = s.recv(128)
    if data:
        print(str(data, 'utf8'), end='')
    else:
        break

s.close()