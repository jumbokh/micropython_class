import machine
from machine import SoftI2C, Pin
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
# Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/
from HCSR04 import HCSR04
from time import sleep

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
# ESP32
sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

# ESP8266
#sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

while True:
    lcd.clear()
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    lcd.putstr('{:.3} cm'.format(distance))
    sleep(1)
