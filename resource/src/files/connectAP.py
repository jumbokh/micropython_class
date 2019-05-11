def connectAP(ssid,pwd):
   import network
   wlan = network.WLAN(network.STA_IF)
   if not wlan.isconnected():
      wlan.active(True)
      wlan.connect(ssid,pwd)
      wlan.ifconfig(('192.168.43.88',
                    '255.55.255.0',
                    '192.168.43.254',
                    '8.8.8.8'))
      while not wlan.isconnected():
            pass
   print('network config:', wlan.ifconfig())

connectAP('informatics', '0953313123')