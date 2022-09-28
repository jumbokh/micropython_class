import network
import config

def connect_wifi(ssid, passwd):
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    if not sta.isconnected():
       print("Connecting to network...")
       sta.connect(ssid, passwd)
       while not sta.isconnected():
          pass
    print("network config:", sta.ifconfig())

SSID = config.SSID        # WiFi名稱
PASSWORD = config.KEY    # WiFi密碼
connect_wifi(SSID, PASSWORD)