import pigpio
from time import sleep

pi = pigpio.pi()

#set GPIO pins
channel = 17

light_on = 10;        #seconds
frequency =  100000;    #seconds 

pi.set_mode(17,pigpio.INPUT)
pi.set_PWM_dutycycle(17,128)

pi.set_PWM_frequency(17,5000)

print(pi.get_PWM_frequency(17))

sleep(light_on)

pi.write(channel,0)

