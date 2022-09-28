import machine, utime,ssd1306

hw_i2c1 = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))# machine.I2C(0x3c, freq=200000)        
oled096=ssd1306.SSD1306_I2C(128, 64, hw_i2c1)
oled096.fill(0) 
oled096.text('~ TEMP & HUMID ~',0,0)
oled096.text('Temp =    C',0,16)
oled096.text('Humid=    %',0,32)
oled096.text("PM2.5 =    ",0,48)
oled096.show()