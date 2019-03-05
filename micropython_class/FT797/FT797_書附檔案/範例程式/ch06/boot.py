# This file is executed ...
import esp
esp.osdebug(None)
import gc

def connectAP(ssid, pwd):
   import network
   wlan = network.WLAN(network.STA_IF)

   if not wlan.isconnected():
      wlan.active(True)       
      wlan.connect(ssid, pwd)

      while not wlan.isconnected():
         pass

   print('network config:', wlan.ifconfig())

connectAP('無線網路ID', '密碼')

import webrepl
webrepl.start()
gc.collect()
