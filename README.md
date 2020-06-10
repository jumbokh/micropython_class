### Micropython class
#### 講義
* [ppt1](https://github.com/jumbokh/micropython_class/blob/master/Micropython_20200613.pptx)
* [ppt2](https://github.com/jumbokh/micropython_class/blob/master/MicroPython102%20IOT%E5%85%A5%E9%96%80.pptx)
* [MicroPython中文教程.pdf](https://github.com/jumbokh/micropython_class/blob/master/doc/MicroPython%E4%B8%AD%E6%96%87%E6%95%99%E7%A8%8B.pdf)
### 設定
* 1. [方法一: winpython](README-1.md)
* 2. [方法二: uPyCraft](http://docs.dfrobot.com.cn/upycraft/) # [在 ESP32開發板上 使用 uPyCraft 快速燒錄及編寫程式](https://davistseng.blogspot.com/2017/12/esp32-upycraft.html)
### 方法三: 手動安裝
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
