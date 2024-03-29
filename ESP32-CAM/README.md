## AI-THINKER 官網
* [ESP32-CAM](http://wiki.ai-thinker.com/esp32-cam)
* [PRODUCT DETAILS](https://www.seeedstudio.com/ESP32-CAM-Development-Board-with-camer-p-3153.html)
## 
* 使用 esp32cam-firmware.bin
* 先測試安裝 picoweb, 參考 [ESP32 MicroPython: HTTP Webserver with Picoweb](https://techtutorialsx.com/2017/09/01/esp32-micropython-http-webserver-with-picoweb/)
* 須注意 upip 安裝 library
##
* 測試 [Webcam with ESP32-CAM and MicroPython](https://github.com/tsaarni/esp32-micropython-webcam)
<pre>
# 記得修改 SSID, Key
export AMPY_PORT=/dev/ttyUSB0
ampy put boot.py
ampy put webcam.py
</pre>
## 重開後, 使用 putty 等終端機連接, 安裝 library
<pre>
import upip
upip.install('picoweb')  # tested with 1.5.2
upip.install('micropython-ulogging')
upip.install('ujson')
</pre>
##
## 參考
* [esp32-cam source](https://kopimojo.blogspot.com/2019/10/micropython-v1.html)
* [ESP32-CAM | ESP32 Camera Module with Face Recognition](https://robotzero.one/esp32-camera-module/)
* [Using a Camera with the ESP32](https://www.hackster.io/news/using-a-camera-with-the-esp32-9d6994b34a2b)
