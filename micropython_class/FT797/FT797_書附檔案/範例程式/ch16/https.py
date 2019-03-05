# -*- coding: utf-8 -*-

"""
   程式說明請參閱16-35頁
"""

import socket
import ussl as ssl

url = 'https://micropython.org/ks/test.html'
 
httpHeader = b'''\
GET /{path} HTTP/1.0
Host:{host}
User-Agent: MicroPython

'''

_, _, host, path = url.split('/', 3)
addr = socket.getaddrinfo(host, 443)[0][-1]
s = socket.socket()
s.connect(addr)
s = ssl.wrap_socket(s)
s.write(httpHeader.format(path=path, host=host))

while True:
    data = s.read(128)
    if data:
        print(str(data, 'utf8'), end='')
    else:
        break
s.close()