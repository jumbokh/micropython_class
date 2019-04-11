from machine import PWM, Pin

class Servo:
    def __init__(self, pin, min=500, max=2400, range=180):
        self.servo = PWM(Pin(pin), freq=50)
        self.period = 20000
        self.minDuty = self.__duty(min)
        self.maxDuty = self.__duty(max)
        self.unit = (self.maxDuty - self.minDuty)/range

    def __duty(self, value):
        return int(value/self.period * 1024)

    def rotate(self, degree=90):
        val = round(self.unit * degree) + self.minDuty
        val = min(self.maxDuty, max(self.minDuty, val))
        self.servo.duty(val)
