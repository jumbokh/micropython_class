### Micropython class
#### 講義
* [ppt1](https://github.com/jumbokh/micropython_class/blob/master/Micropython_20200613.pptx)
* [ppt2](https://github.com/jumbokh/micropython_class/blob/master/MicroPython102%20IOT%E5%85%A5%E9%96%80.pptx)
* [MicroPython中文教程.pdf](https://github.com/jumbokh/micropython_class/blob/master/doc/MicroPython%E4%B8%AD%E6%96%87%E6%95%99%E7%A8%8B.pdf)
#### 設定/IDE
* 1. [方法一: winpython](https://github.com/jumbokh/micropython_class/blob/master/readme-wpy.md)
* 2. [方法二: uPyCraft](http://docs.dfrobot.com.cn/upycraft/) # [在 ESP32開發板上 使用 uPyCraft 快速燒錄及編寫程式](https://davistseng.blogspot.com/2017/12/esp32-upycraft.html)
* 3. [方法三: Thonny](https://thonny.org/)  # [Thonny WiKi](https://github.com/thonny/thonny/wiki)
* 4. 方法四: 手動安裝
#### Micropython 韌體
* [MicroPython downloads](http://micropython.org/download/)
#### 安裝軟體
* Windows 環境
    * 1. [anaconda](https://www.anaconda.com/products/individual) ## 建立虛擬環境
    * 2. pip install pyserial esptool jupyter
    * 3. [ampy](https://ithelp.ithome.com.tw/articles/10203046) ## pip3 install adafruit-ampy
    * 4. [putty 終端機](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
    * 5. [git bash](https://git-scm.com/download/win)
    * 6. [jupyter_micropython_kernel](https://github.com/goatchurchprime/jupyter_micropython_kernel.git)
        * pip install -e jupyter_micropython_kernel
        * python -m jupyter_micropython_kernel.install
        * jupyter kernelspec list
        * jupyter notebook
#### Lab: 
* Lab list:
    * [demo files](https://github.com/jumbokh/micropython_class/tree/master/demo)
    * [ESP32](https://github.com/jumbokh/micropython_class/tree/master/ESP32)
    * [ESP32-CAM](https://github.com/jumbokh/micropython_class/tree/master/ESP32-CAM)
    * boot.py
<pre>
%sendtofile boot.py
import network
import ubinascii
import time
sta = network.WLAN(network.STA_IF)
sta.active(True)

SSID='your-ssid'
KEY='your-key'
print(sta.active())
sta.connect(SSID,KEY)

mac = ubinascii.hexlify(sta.config('mac'),':').decode()
print(mac)
for i in range(20):
    time.sleep(0.5)
    if sta.isconnected():
        break
print(sta.ifconfig())
print('ESP32 Started.')
</pre>
#### Starting
* esptool
    * erase: python -m esptool erase_flash
    * burn firmware: python -m esptool --port COM4 --chip esp32 write_flash 0x1000 esp32-firmware.bin
* examples:
    * [rebuild ESP32](https://github.com/jumbokh/micropython_class/blob/master/ESP32/0.%20rebuild_esp32.ipynb)
    * [LED Blink](https://github.com/jumbokh/micropython_class/blob/master/ESP32/Lab1_LED.ipynb)
    * [Button](https://github.com/jumbokh/micropython_class/blob/master/ESP32/Lab3_button.ipynb)
    * [DHT11 Test](https://github.com/jumbokh/micropython_class/blob/master/ESP32/LAB4_DHT11.ipynb)
    * [MQTT -- DHT11](https://github.com/jumbokh/micropython_class/tree/master/ESP32/MQTT)
        * 安裝 [MQTT Dashboard app](https://apkpure.com/tw/iot-mqtt-dashboard/com.thn.iotmqttdashboard)
    * [picoweb](https://github.com/jumbokh/micropython_class/tree/master/ESP32/Web)
##
### 參考
* [Micropython for ESP32 ](https://docs.espressif.com/projects/esp-idf/zh_CN/v4.0.1/get-started/index.html)
* [Firmware buildup](https://github.com/shariltumin/esp32-cam-micropython/tree/master/esp32-cam-1-11-498)
* [MicroPython: Taking photos with an ESP32-CAM](https://lemariva.com/blog/2019/09/micropython-how-about-taking-photo-esp32)
* [Ubuntu18.04：搭建ESP32 MicroPython编译环境](https://codeleading.com/article/38851328254/)
* [Rest example](https://gitlab.com/superfly/dawndoor/-/tree/master/src)
* [MicroRESTCli](https://github.com/jczic/MicroRESTCli)
* [快速入门](https://docs.espressif.com/projects/esp-idf/zh_CN/v4.0.1/get-started/index.html)
* [uPyCraft 中的範例](http://docs.dfrobot.com.cn/upycraft/%E7%AC%AC4%E7%AB%A0%E7%BB%BC%E5%90%88%E9%A1%B9%E7%9B%AE.html)
* [Building Qt 5 from Git](https://wiki.qt.io/Building_Qt_5_from_Git#Getting_the_source_code)
* [uPyCraft_PyQt5](https://longervision.github.io/2018/09/15/Tools/uPyCraft_PyQt5/)
* [MicroPython on ESP32 學習筆記 (九) : upip 安裝網頁框架 picoweb 失敗](http://yhhuang1966.blogspot.com/2019/07/micropython-on-esp32-upip-picoweb.html)


