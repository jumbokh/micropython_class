from machine import I2C,Pin
import time
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

#i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

while True:
    lcd.putstr("I2C LCD Tutorial")
    time.sleep(2)
    lcd.clear()
    lcd.putstr("Lets Count 0-10!")
    time.sleep(2)
    lcd.clear()
    for i in range(11):
        lcd.putstr(str(i))
        time.sleep(1)
        lcd.clear()
