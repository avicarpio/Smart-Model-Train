# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO          
from time import sleep

import time
import math

GPIO.setmode(GPIO.BCM)

m1_in1 = 24
m1_in2 = 23
m1_en = 25

GPIO.setup(m1_in1,GPIO.OUT)
GPIO.setup(m1_in2,GPIO.OUT)
GPIO.setup(m1_en,GPIO.OUT)
GPIO.output(m1_in1,GPIO.LOW)
GPIO.output(m1_in2,GPIO.LOW)

p1=GPIO.PWM(m1_en,50)

p1.start(0)
p1.ChangeDutyCycle(0)

last_value = 0

while(1):
    
    file = open("/var/www/html/sliderValue.txt", "r")
    sliderValue = int(file.readline())
    file.close()
    if last_value != sliderValue:
        if sliderValue < 0:
            GPIO.output(m1_in1,GPIO.LOW)
            GPIO.output(m1_in2,GPIO.HIGH)
        else:
            GPIO.output(m1_in1,GPIO.HIGH)
            GPIO.output(m1_in2,GPIO.LOW)

        p1.ChangeDutyCycle(math.abs(sliderValue))

        last_value = sliderValue

    sleep(0.05)