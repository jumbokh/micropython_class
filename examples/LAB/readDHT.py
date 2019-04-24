from machine import Pin
import dht     
import time

p5=Pin(5, Pin.IN)
d=dht.DHT11(p5)        #建立 DHT11 物件

print('Measuring....')
d.measure()                  #重新測量溫溼度
time.sleep(0.5)
t=d.temperature()        #讀取攝氏溫度
h=d.humidity()             #讀取相對溼度
print('Temperature=', t, 'C', 'Humidity=', h, '%')
