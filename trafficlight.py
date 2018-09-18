import sys, time
import RPi.GPIO as GPIO

#Final Code For Server End

GPIO.setwarnings(False) #Disable warnings
GPIO.setmode(GPIO.BCM) #Referring to pins in the Broadcom SOC channel - the numbers after GPIO
GPIO.setup(18, GPIO.OUT) #GPIO pin # is 18 -- Red
GPIO.setup(8, GPIO.OUT) #GPIO pin # is 8 -- Yellow
GPIO.setup(21, GPIO.OUT) #GPIO pin # is 21 -- Green

from flask
import Flask #Importing Flask

app=Flask(__name__)

#Red
@
app.route('/redled') #web route to red led
def redled():
    GPIO.output(18, True) #Red is on

@app.route('yellowled') #web route to yellow led
def yellowled():
    GPIO.output(8, True) #Yellow is on

@app.route('greenled') #web route to green led
def greenled():
    GPIO.output(21, True) #Green is on

@app.route('off') #web route to turning light(s) off
GPIO.output(18, False) #Red is off
GPIO.output(8, False) #Yellow is off
GPIO.output(21, False) #Green is off

@app.route('cycle') #web route to cycle through all the lights
#Time to cycle
while True: #Let's do a loop
    GPIO.output(18, True) #Red is on
    time.sleep(4) #Red continues on for 2 secs
    GPIO.output(18, False) #Red is off
    GPIO.output(21, True) #Green is on
    time.sleep(4) #Green is on for 2 secs
    GPIO.output(21, False) #Green is off
    GPIO.output(8, True) #Yellow is on
    time.sleep(4) #On for 4 sec
    GPIO.output(8, False) #Yellow is off

