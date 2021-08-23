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



while(1):
    
    if velocitat == 0:
        GPIO.output(m1_in1,GPIO.LOW)
        GPIO.output(m1_in2,GPIO.LOW)
        GPIO.output(m2_in1,GPIO.LOW)
        GPIO.output(m2_in2,GPIO.LOW)
        print("STOP!!")
    else:
    
        if math.sin(math.radians(angle)) > 0 :
            #Forward
            GPIO.output(m1_in1,GPIO.HIGH)
            GPIO.output(m1_in2,GPIO.LOW)
            GPIO.output(m2_in1,GPIO.HIGH)
            GPIO.output(m2_in2,GPIO.LOW)
        else:
            #Backward
            GPIO.output(m1_in1,GPIO.LOW)
            GPIO.output(m1_in2,GPIO.HIGH)
            GPIO.output(m2_in1,GPIO.LOW)
            GPIO.output(m2_in2,GPIO.HIGH)
        if math.cos(math.radians(angle)) > 0:
            print("Posit: " + str(angle) + " | " + str(velocitat * (1 - math.cos(math.radians(angle)))) + " COS: " + str(math.cos(math.radians(angle))))
            p1.ChangeDutyCycle(velocitat * (1 - math.cos(math.radians(angle))))
            p2.ChangeDutyCycle(velocitat)
        else:
            print("Negat: " + str(angle) + " | " + str(velocitat * (1 - abs(math.cos(math.radians(angle))))) + " COS: " + str(math.cos(math.radians(angle))))
            p2.ChangeDutyCycle(velocitat * (1 - abs(math.cos(math.radians(angle)))))
            p1.ChangeDutyCycle(velocitat)
    
    
