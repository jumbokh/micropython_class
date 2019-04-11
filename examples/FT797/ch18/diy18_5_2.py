# -*- coding: utf-8 -*-

"""
   程式說明請參閱18-30頁
"""

def setUTC8Time():
    import time, ntptime, machine
    t = ntptime.time() + 28800
    tm = time.localtime(t)
    machine.RTC().datetime(tm[0:3] + (0, ) + tm[3:6] + (0,))
    print(time.localtime())
