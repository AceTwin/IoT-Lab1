import sys, time
import RPi.GPIO as GPIO

#Testing for 3 LED

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
while True: #Loop Time!
    GPIO.output(18, True) #Red is on
    GPIO.output(21, True) #Green is on
    GPIO.output(8, True) #Yellow is on

time.sleep(1) #Off for 1 sec
