# -*- coding: utf-8 -*-

"""
   程式說明請參閱18-33頁
"""

import machine
import time

rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
rtc.alarm(rtc.ALARM0, 10000)

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')
else:
    print('power on or hard reset')

for i in range(5):
    print('Going sleep in {} sec.'.format(5-i))
    time.sleep(1)

machine.deepsleep()