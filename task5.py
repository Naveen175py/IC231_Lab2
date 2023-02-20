import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

channel = 17

GPIO.setup(channel, GPIO.OUT)

GPIO.output(channel, GPIO.LOW)
sleep(0.4)

GPIO.output(channel, GPIO.HIGH)
sleep(0.1)

GPIO.output(channel, GPIO.LOW)
sleep(0.5)

GPIO.cleanup(channel)

