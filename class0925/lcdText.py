import machine
from machine import SoftI2C, Pin
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

heart = bytearray([0x00,0x00,0x1B,0x1F,0x1F,0x0E,0x04,0x00])
face = bytearray([0x00,0x00,0x0A,0x00,0x11,0x0E,0x00,0x00])
lcd.custom_char(0, heart)
lcd.custom_char(1, face)
lcd.putstr(chr(0)+" ESP32 with I2C LCD "+chr(1))
