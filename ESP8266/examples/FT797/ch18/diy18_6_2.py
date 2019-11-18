# -*- coding: utf-8 -*-

"""
   程式說明請參閱18-36頁
"""

import machine
import time

rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
rtc.alarm(rtc.ALARM0, 10000)

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    if rtc.memory() != b'':
        counter = int(rtc.memory())
        counter += 1
        rtc.memory(bytes(str(counter), 'utf-8'))
    else: 
        rtc.memory(b'0')

    print('woke from a deep sleep')
    print('counter:', counter)
else:
    print('power on or hard reset')
    rtc.memory(b'')

for i in range(5):
    print('Going sleep in {} sec.'.format(5-i))
    time.sleep(1)

machine.deepsleep()