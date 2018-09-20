#!/usr/bin/python
from flask_api import FlaskAPI
from flask import Flask, request, render_template
import sys, time
import RPi.GPIO as GPIO

#Final Code For Server End

#Reference Code: 
#https://www.canakit.com/Media/CanaKit-Raspberry-Pi-Quick-Start-Guide-3.2.pdf
#https://pythonspot.com/flask-with-static-html-files/
#https://www.cloudways.com/blog/internet-of-things-remote-control-appliances-using-raspberry-pi/
#https://docs.dataplicity.com/docs/control-gpios-using-rest-api

GPIO.setwarnings(False) #Disable warnings
GPIO.setmode(GPIO.BCM) #Referring to pins in the Broadcom SOC channel - the numbers after GPIO
GPIO.setup(18, GPIO.OUT) #GPIO pin # is 18 -- Red
GPIO.setup(8, GPIO.OUT) #GPIO pin # is 8 -- Yellow
GPIO.setup(21, GPIO.OUT) #GPIO pin # is 21 -- Green

#app = FlaskAPI(__name__)
app = Flask(__name__)

#Initial Stage -- everything off
GPIO.output(18, False) #Red is off
GPIO.output(8, False) #Yellow is off
GPIO.output(21, False) #Green is off

@app.route('/')
def root():
    return render_template('/index.html')

#Red
@app.route('/redled') #web route to red led
def redled():
    GPIO.output(18, True) #Red is on
    return '<meta http-equiv="Refresh" content="0; url=/">Command Sent'

@app.route('/yellowled') #web route to yellow led
def yellowled():
    GPIO.output(8, True) #Yellow is on
    return '<meta http-equiv="Refresh" content="0; url=/">Command Sent'

@app.route('/greenled') #web route to green led
def greenled():
    GPIO.output(21, True) #Green is on
    return '<meta http-equiv="Refresh" content="0; url=/">Command Sent'

@app.route('/off') #web route to turning light(s) off
def off():
    GPIO.output(18, False) #Red is off
    GPIO.output(8, False) #Yellow is off
    GPIO.output(21, False) #Green is off
    return '<meta http-equiv="Refresh" content="0; url=/">Command Sent'

@app.route('/cycle') #web route to cycle through all the lights
def cycle():
    #Initial Stage -- everything is off
    GPIO.output(18, False) #Red is off
    GPIO.output(8, False) #Yellow is off
    GPIO.output(21, False) #Green is off
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
    #Keep on cycling but return to the initial web page for another command
    return '<meta http-equiv="Refresh" content="0; url=/">Command Sent'

if __name__ == "__main__":
    app.run()
