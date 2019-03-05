# -*- coding: utf-8 -*-

"""
   程式說明請參閱9-15頁
"""

from machine import Pin, PWM
import time

buzzer = PWM(Pin(14))

pitches = {
    'C5':523,
    'D5':587,
    'E5':659,
    'F5':698,
    'G5':784,
    'A5':880,
    'B5':988,
    'S':0
}

melody = (
    ('E5',100),('S',100),('E5',100),('S',300),('E5',100),('S',300),
    ('C5',100),('S',100),('E5',100),('S',300),('G5',100)
)

for tone, tempo in melody:

    if tone == 'S':
        buzzer.duty(0)
    else:
        buzzer.duty(900)
        buzzer.freq(pitches[tone])

    time.sleep_ms(tempo)

buzzer.deinit()