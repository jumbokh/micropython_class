### Micropython 安裝程序
#
#### 工具程式：
* [anaconda](https://www.anaconda.com/distribution/)
* [Flasher64](https://github.com/nodemcu/nodemcu-flasher/tree/master/Win64/Release)
* [putty 終端機程式](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
* [Micropython Kernel](https://github.com/goatchurchprime/jupyter_micropython_kernel.git)
* [git bash](https://git-scm.com/download/win)
* [驅動程式](https://github.com/jumbokh/micropython_class/blob/master/CP210x_Windows_Drivers_with_Serial_Enumeration.zip)
* [windows platform SDK](https://github.com/jumbokh/micropython_class/blob/master/Install/NDP46-KB3045560-Web.zip)
#
#### 基本檔案：
* [boot.py](https://github.com/jumbokh/micropython_class/blob/master/Install/boot.py)
* [main.py](https://github.com/jumbokh/micropython_class/blob/master/Install/main.py)
* [webtool.html](https://github.com/jumbokh/micropython_class/blob/master/Install/webtool.html)
#
#### 安裝步驟：
* 下載及安裝工具程式
* 下載[韌體檔案](https://github.com/jumbokh/micropython_class/blob/master/micropython_class/binary/esp8266-20190125-v1.10.bin)
*  以 Flasher64 燒錄韌體
![image](https://github.com/jumbokh/micropython_class/blob/master/Install/images/%E7%87%92%E9%8C%84main.JPG)
![image](https://github.com/jumbokh/micropython_class/blob/master/Install/images/%E7%87%92%E9%8C%84config.JPG)
![image](https://github.com/jumbokh/micropython_class/blob/master/Install/images/%E7%87%92%E9%8C%84Advance.JPG)
#
#### 燒錄不成功時，清空 flash (在 anaconda prompt 中執行)
###### 相關模組
* python -m pip install --upgrade pip
* pip install pyserial esptool
* python -m esptool --port COM3 erase_flash
#
#### [Google 雲端：WPy-0524-R1](https://drive.google.com/open?id=1JjDOW1SdlqrCXyX2vjAydp3E2eedKtsI)
###  [kernel 參考](https://github.com/maloyang/20181116_smart-car/blob/master/smart-car-workshop.ipynb)
#
#### 佈建Windows執行環境
* conda create -n venv python=3.5
* activate venv
* mkdir micropython
* cd micropython
* pip install numpy matplotlib pyserial
* python -m pip install --upgrade pip
* pip install adafruit-ampy jupyter
* git clone https://github.com/goatchurchprime/jupyter_micropython_kernel.git
* pip install -e jupyter_micropython_kernel
* jupyter kernelspec list
![image](images/kernels.JPG)
#
#### test：
* putty 終端機
###### 開啟putty
![image](images/putty.JPG)
###### 設定連接埠
![image](images/putty_serial.JPG)
###### 連接
###### 嘗試按 CTRL-C
###### 出現提示符號
###### >>> 
###### >>> import uos
###### >>> uos.uname()
#
* ampy test:
###### ampy --port COM4 ls
![image](images/kernels.JPG)
#
* 設定 webrepl
###### MicroPython v1.10-8-g8b7039d7d on 2019-01-26; ESP module with ESP8266
###### Type "help()" for more information.
###### >>> import webrepl_setup
###### WebREPL daemon auto-start status: disabled
######
###### Would you like to (E)nable or (D)isable it running on boot?
###### (Empty line to quit)
###### > e
###### To enable WebREPL, you must set password for it
###### New password (4-9 chars): 1234
###### Confirm password: 1234
###### Changes will be activated after reboot
###### Would you like to reboot now? (y/n)
###### >>> import webrepl
###### >>> webrepl.start()
#
* 設定網路
###### >>> import network
###### >>> sta = network.WLAN(network.STA_IF)
###### >>> sta.ifconfig()
#
###### [參考](https://www.instructables.com/id/Micropython-on-ESP-Using-Jupyter/)
