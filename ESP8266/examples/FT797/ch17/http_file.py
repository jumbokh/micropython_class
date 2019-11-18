# -*- coding: utf-8 -*-

"""
   程式說明請參閱17-14頁
"""

import socket, os, gc

HOST = '0.0.0.0'
PORT = 80
WWWROOT = '/www/'

httpHeader = '''HTTP/1.0 200 OK
Content-type: {}
Content-length: {}

'''

mimeTypes = {
    '.txt'  : 'text/plain',
    '.htm'  : 'text/html',
    '.html' : 'text/html',
    '.css'  : 'text/css',
    '.js'   : 'application/javascript',
    '.xml'  : 'application/xml',
    '.json' : 'application/json',
    '.jpg'  : 'image/jpeg',
    '.png'  : 'image/png',
    '.gif'  : 'image/gif',
    '.svg'  : 'image/svg+xml',
    '.ico'  : 'image/x-icon'
}

def checkFileSize(path):
    try:
        s = os.stat(path)

        if s[0] != 16384:
            fileSize = s[6]
        else:
            fileSize = None
        return fileSize
    except:
        return None

def checkMimeType(fileName):
    fileName = fileName.lower()

    for ext in mimeTypes:
        if fileName.endswith(ext):
            return mimeTypes[ext]
    return None

def err(socket, code, msg):
    socket.write("HTTP/1.1 "+code+" "+msg+"\r\n\r\n")
    socket.write("<h1>"+msg+"</h1>")

def handleRequest(client):
    req = client.recv(1024).decode('utf8')
    firstLine = req.split('\r\n')[0]
    print(firstLine)
    
    httpMethod = ''
    path = ''

    try:
        httpMethod, path, httpVersion = firstLine.split()

        del httpVersion
    except:
        pass

    del firstLine
    del req

    if httpMethod == 'GET':
        fileName = path.strip('/')

        if fileName == '':
            fileName = 'index.html'
        sendFile(client, fileName)

     else:
        err(client, "501", "Not Implemented")

def sendFile(client, fileName):
    contentType = checkMimeType(fileName)

    if contentType :
        fileSize = checkFileSize(WWWROOT+fileName)

        if fileSize != None:
            f = open(WWWROOT+fileName, 'r')
            httpHeader.format(contentType, fileSize)
            print('file name: ' + WWWROOT+fileName)

            client.write(httpHeader.encode('utf-8'))

            while True:
                chunk = f.read(64)
                if len(chunk) == 0:
                    break
                client.write(chunk)

            f.close()
        else:
            err(client, "404", "Not Found")
    else:
        err(client, "415", "Unsupported Media Type")

def main():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    print('Web server running on port', PORT)

    while True:
        client = s.accept()[0]

        handleRequest(client)

        client.close()
        
        print('Free RAM before GC:', gc.mem_free())
        gc.collect()
        print('Free RAM after GC:', gc.mem_free())

main()
