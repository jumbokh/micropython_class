# -*- coding: utf-8 -*-

"""
   程式說明請參閱17-2頁
"""

import socket

s = socket.socket()
HOST = '0.0.0.0'
PORT = 80
httpHeader = b"""\
HTTP/1.0 200 OK

Welcome to MicroPython!
"""

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)
print("Server running on port ", PORT)

while True:
    client, addr = s.accept()
    print("Client address:", addr)
    
    req = client.recv(1024)
    print("Request:")
    print(req)
    client.send(httpHeader)
    client.close()
    print('-----------------------')