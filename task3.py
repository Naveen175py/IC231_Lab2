import RPi.GPIO as GPIO
from time import sleep 

GPIO.setmode(GPIO.BCM)

channel1 = 17

GPIO.setup(channel1, GPIO.OUT)

light_on = 10
frequency = 1000
GPIO.setup(channel1,frequency)
c = GPIO.PWM(channel1, frequency)
def blink(frequency):
    t=0
    while t<=10:
        c.start(50)
        t+=1/frequency
        sleep(1/frequency)

blink(frequency)

GPIO.cleanup(channel1)