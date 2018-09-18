import sys, time
import RPi.GPIO as GPIO

#Testing for traffic light cycle

GPIO.setwarnings(False) #Disable warnings
GPIO.setmode(GPIO.BCM) #Referring to pins in the Broadcom SOC channel - the numbers after GPIO
GPIO.setup(18, GPIO.OUT) #GPIO pin # is 18 -- Red
GPIO.setup(8, GPIO.OUT) #GPIO pin # is 8 -- Yellow
GPIO.setup(21, GPIO.OUT) #GPIO pin # is 21 -- Green

#Time to cycle

while True: #Let's do a loop
    GPIO.output(18, True) #Red is on
    time.sleep(2) #Red continues on for 2 secs
    GPIO.output(18, False) #Red is off
    GPIO.output(21, True) #Green is on
    time.sleep(2) #Green is on for 2 secs
    GPIO.output(21, False) #Green is off
    GPIO.output(8, True) #Yellow is on
    time.sleep(2) #On for 4 sec
    GPIO.output(8, False) #Yellow is off

#Woohhh they all work! :) 
