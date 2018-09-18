import sys, time
import RPi.GPIO as GPIO

#Testing for 3 LED

GPIO.setwarnings(False) #Disable warnings
GPIO.setmode(GPIO.BCM) #Referring to pins in the Broadcom SOC channel - the numbers after GPIO
GPIO.setup(18, GPIO.OUT) #GPIO pin # is 18 -- Red
GPIO.setup(8, GPIO.OUT) #GPIO pin # is 8 -- Yellow
GPIO.setup(21, GPIO.OUT) #GPIO pin # is 21 -- Green

#Test for blinking LEDs

while True: #Let's do a loop
    GPIO.output(18, True) #Red is on
    GPIO.output(8, True) #Yellow is on
    GPIO.output(21, True) #Green is on
    time.sleep(4) #On for 4 sec
    GPIO.output(18, False) #Red is off
    GPIO.output(8, False) #Yellow is off
    GPIO.output(21, False) #Green is off
    time.sleep(1) #Off for 1 sec

#Woohhh they all work! :) 
