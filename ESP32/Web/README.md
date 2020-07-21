##picoweb on micropython
#### GPIO0 接地, 上電
* 啟動 micropython 虛擬環境
    * Windows: 執行 anaconda-command-prompt(ESP32-CAM)
    * 確定有安裝 pyserial , esptool, ampy ==> pip list
        * pip install pyserial esptool adafruit-ampy
* erase flash: python -m esptool erase_flash
* write flash: python -m  esptool write_flash 0x1000 ../esp32-idf3-20200609-unstable-v1.12-513-g51fd6c977.bin
#### 斷電, GPIO0 不接地， 重新上電
* 安裝 啟動 putty 終端機
    * >>> import os
    * >>> os.listdir()
    * ['boot.py']
* 上傳 boot.py webapp.py ## 啟用網路, 記得修改 boot.py 中的 SSID, Key
    * ampy --port COM4 ls
    * ampy --port COM4 put boot.py
    * ampy --port COM4 put webapp.py
    * 再次使用 putty 監看網路啟用情形, 並紀錄獲得之 IP
* 安裝 picoweb 相關網路模組, 使用 putty 終端機
<pre>
# 進入 esp32 micropython 提示符號 >>>
1. 安裝 picoweb 套件：
>>>  import os
>>> os.listdir()
>>> import upip
>>> upip.install('picoweb')
>>> os.listdir()
['boot.py', 'webapp.py', 'lib']
>>> os.chdir('lib')
>>> os.listdir()
['picoweb', 'uasyncio', 'pkg_resources.py']
# 測看看
>>> import uasyncio   
>>> import pkg_resources    
>>> import picoweb
#
2. 安裝 pycopy-ulogging 套件 : 
>>> upip.install('micropython-logging')
>>> upip.install('pycopy-ulogging') 
安裝好匯入 ulogging 檢視其成員 :

>>> import ulogging 
>>> dir(ulogging) 
['__class__', '__name__', '__file__', 'DEBUG', 'info', 'sys', 'debug', 'getLogger', 'CRITICAL', 'ERROR', 'WARNING', 'INFO', 'NOTSET', '_level_dict', '_stream', 'Logger', '_level', '_loggers', 'basicConfig']
>>> os.getcwd() 
'/lib' 
>>> os.listdir() 
['picoweb', 'uasyncio', 'pkg_resources.py', 'ulogging.py']
#
3. 安裝  utemplate 模板套件 :
>>> upip.install('utemplate')
#
# 重開, 測試網頁
</pre>
##
### 參考
* [picoweb](https://github.com/pfalcon/picoweb)
* [uasyncio error topics](https://forum.micropython.org/viewtopic.php?t=6002)
* [Running Picoweb on hardware devices](https://github.com/peterhinch/micropython-samples/blob/master/PICOWEB.md)
