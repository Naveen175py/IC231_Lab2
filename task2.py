import RPi.GPIO as GPIO
from time import sleep 

GPIO.setmode(GPIO.BCM)

channel1 = 17

GPIO.setup(channel1, GPIO.OUT)

GPIO.setup(channel1,100)
c = GPIO.PWM(channel1, 100)
def task_2(duty_cycle):
    t=0
    while t<=10:
        c.start(duty_cycle)
        t+=1/100


duty_cycle = 25
task_2(duty_cycle)

GPIO.cleanup(channel1)