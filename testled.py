import sys, time
import RPi.GPIO as GPIO

#Testing for 1 LED

GPIO.setwarnings(False) #Initial State
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) #GPIO pin # is 18.

#Test for blinking LED

while True:
    GPIO.output(18, True)
    time.sleep(1) #On for 1 sec
    GPIO.output(18, False)
    time.sleep(1) #Off for 1 sec
