# -*- coding: utf-8 -*-

"""
   程式說明請參閱10-22頁
"""

from machine import Timer
import servo
import random
import time

class Target(servo.Servo):
    def __init__(self, pin, upTime=(3,6), downTime=(3,10)):
        super().__init__(pin)
        self.upTime = upTime
        self.downTime = downTime
        self.running = False
        self.rotate(0)
        self.state = 'down'
        self.tim = Timer(-1)

    def turn(self, t):
        if self.state == 'down':
            print('going up')
            self.rotate(90)
            time.sleep(0.15)
            self.state = 'up'
        else:
            print('going down')
            self.rotate(0)
            time.sleep(0.15)
            self.state = 'down'

        t.deinit()
        self.startTimer()

    def startTimer(self):
        if self.state == 'up':
            r = random.randint(self.upTime[0], self.upTime[1]) * 1000
        else:
            r = random.randint(self.downTime[0], self.downTime[1]) * 1000

        print("random time: " + str(r) + "ms")

        if self.tim == None:
            self.tim = Timer(-1)
        self.tim.init(period=r, mode=Timer.ONE_SHOT, callback=self.turn)

    def start(self):
        if self.running:
            return
        else:
            self.running = True
            self.startTimer()

    def stop(self):
        if not self.running:
            return
        else:
            self.running = False
            self.tim.deinit()
            self.tim = None
            self.rotate(0)
            self.state = 'down'
            print('target stopped')
