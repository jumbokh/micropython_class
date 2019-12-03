* #from machine import ADC, Pin
* import machine

* adc = ADC(Pin(36))          # 在ADC引腳上創建ADC物件
* adc.read()                  # 讀取測量值, 0-4095 表示電壓從 0.0v - 1.0v

* adc.atten(ADC.ATTN_11DB)    # 設置 11dB 衰減輸入 (測量電壓大致從 0.0v - 3.6v)
* adc.width(ADC.WIDTH_9BIT)   # 設置 9位 精度輸出 (返回值 0-511)
* a = adc.read()
* print(a)           # 獲取重新配置後的測量值
* vi = 3.3 * 120/(120+200)
* vo = (a /255.0) * vi
* print(vi,vo)
##
### LED + PWM
<pre>
from machine import Pin, ADC, PWM
from time import sleep

led = Pin(2, Pin.OUT)

#Configure ADC for ESP32
pot = ADC(Pin(36))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)

#Configure ADC for ESP
#pot = ADC(0)

led_pwm = PWM(Pin(2),5000)

while True:
   pot_value = pot.read()
   led_pwm.duty(pot_value)
   sleep(0.1)
</pre>
##
### 光敏電阻
* from machine import ADC, Pin
* import time

* p2 = Pin(15, Pin.OUT)
* adc = ADC(Pin(36))            # create ADC object on ADC pin
* while True:
*      if adc.read() > 500:
*             p2.value(1)
*      time.sleep(2)
*      p2.value(0)
