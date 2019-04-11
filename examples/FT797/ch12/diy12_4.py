# -*- coding: utf-8 -*-

"""
   程式說明請參閱12-25頁
"""

import ssd1306
import framebuf
from machine import I2C, Pin

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 48, i2c)

img = [ 0x00, 0x32, 0x49, 0x79, 0x41, 0x3E, 0x00, 0x00 ]
# img =[ 0x38, 0x44, 0x04, 0x34, 0x54, 0x54, 0x38, 0x00 ]
buffer = bytearray(img)

fb = framebuf.FrameBuffer(buffer, 8, 8, framebuf.MONO_VLSB)
# fb = framebuf.FrameBuffer(buffer, 8, 8, framebuf.MONO_HLSB)
oled.fill(0)
oled.framebuf.blit(fb, 30, 20)
oled.framebuf.blit(fb, 90, 20)

oled.show()