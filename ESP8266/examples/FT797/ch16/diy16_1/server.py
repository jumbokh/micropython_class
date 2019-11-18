# -*- coding: utf-8 -*-

"""
   程式說明請參閱16-19頁
"""

import socket
HOST = 'localhost'
PORT = 5438
s = socket.socket()
s.bind((HOST, PORT))
s.listen(5)
print('{}伺服器在{}埠開通了！'.format(HOST, PORT))
client, addr = s.accept()
print('用戶端位址：{}，埠號：{}'.format(addr[0], addr[1]))

while True:
    msg = client.recv(100).decode('utf8')
    print ('收到訊息：' + msg)
    reply = ''

    if msg == '你好':
        reply = b'Hello!'
    elif msg == '再見':
        client.send(b'quit')
        break
    else:
        reply = b'what??'

    client.send(reply)

client.close()