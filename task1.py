import RPi.GPIO as GPIO
from time import sleep 

GPIO.setmode(GPIO.BCM)

channel1=17

GPIO.setup(channel1, GPIO.OUT)
light_on = 10

def blink(frequency):
    t=0
    while t<=10:
        GPIO.output(channel1, GPIO.HIGH)
        sleep(1/frequency)
        GPIO.output(channel1, GPIO.LOW)
        sleep(1/frequency)
        t+=2/frequency

frequency = 1000
blink(frequency)

GPIO.cleanup(channel1)