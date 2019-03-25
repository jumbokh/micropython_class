### Micropython 安裝程序
#
#### 工具程式：
* [anaconda](https://www.anaconda.com/distribution/)
* [Flasher64](https://github.com/nodemcu/nodemcu-flasher/tree/master/Win64/Release)
* [putty 終端機程式](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
* [Micropython Kernel](https://github.com/goatchurchprime/jupyter_micropython_kernel.git)
* [git bash](https://git-scm.com/download/win)
#
#### 基本檔案：
* [boot.py]()
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
#### 使用打包好的整合系統進行測試
#
* 下載/解開： [winpython 下之 WPy-3710-jumbo.zip](https://github.com/jumbokh/micropython_class/blob/master/winpython/WPy-3710-jumbo.zip)
* 參考 winpython 下之 [README.md 說明](https://github.com/jumbokh/micropython_class/blob/master/winpython/README.md)
#
#### test：
* putty 終端機
###### 開啟putty
![image](https://github.com/jumbokh/micropython_class/blob/master/Install/images/putty.JPG)
###### 設定連接埠
![image](https://github.com/jumbokh/micropython_class/blob/master/Install/images/putty_serial.JPG)
###### 連接
###### 嘗試按 CTRL-C
###### 出現提示符號
###### >>> 
###### >>> import uos
###### >>> uos.uname()
#
* ampy test:
###### ampy --port COM4 ls
![image](https://github.com/jumbokh/micropython_class/blob/master/Install/images/kernels.JPG)
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
