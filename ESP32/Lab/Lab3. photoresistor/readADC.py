from machine import ADC, Pin
import utime

led = 2
pOutled = Pin(led, Pin.OUT)
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
adc.width(ADC.WIDTH_9BIT)   # set 9 bit return values (returned range 0-511)
while True:
  adc0 = adc.read()
  print(adc0)
  if adc0 < 300:            # 光線足夠亮, 熄燈
      pOutled.value(0)
  else:                     # 光線太暗, 亮燈
      pOutled.value(1)
  utime.sleep(1)