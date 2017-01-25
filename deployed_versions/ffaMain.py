#!/usr/bin/python

# new script to welcome FFA students to UIdaho Library 
# FFA motto, see https://www.ffa.org/about/who-we-are/mission-motto
# based on Vandal Poem of the Day poemBot Printer V3. 
# see http://poetry.lib.uidaho.edu/  
# adapted from Adafruit Python-Thermal-Printer main.py
# https://github.com/adafruit/Python-Thermal-Printer
# this script is designed to run on a headless Raspberry Pi connected to a thermal printer 
# must be run as sudo 

from __future__ import print_function
import RPi.GPIO as GPIO
import subprocess, time, Image
from thermalPrinter import *

# printer and button set up
ledPin       = 18
buttonPin    = 23
holdTime     = 2     # Duration for button hold (shutdown)
tapTime      = 0.01  # Debounce time for button taps
printer      = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

motto = """Learning to Do,
Doing to Learn,
Earning to Live,
Living to Serve.
"""

event = 'Welcome FFA 2016!'
mill = 'The MILL @ UIdaho Library'
website = 'mill.lib.uidaho.edu'

# Print out called on tap 
def printOut():
    # print image
    printer.printImage(Image.open('FFA_print.png'), True)
    printer.setSize('S')
    printer.justify('C')
    printer.println(motto)
    # printer.println(' ')
    printer.justify('C')
    printer.boldOn()
    printer.println(event)
    printer.boldOff()
    printer.justify('C')
    # printer.println(motto)
    printer.println(' ')
    # printer.writeBytes(0x1B, 0x21, 0x1)
    printer.println(mill)
    printer.println(website)
    printer.println(' ')
    printer.println(' ')
    printer.feed(3)

# Called when button is briefly tapped.  
def tap():
  GPIO.output(ledPin, GPIO.HIGH)  # LED on while working
  printOut()
  GPIO.output(ledPin, GPIO.LOW)

# Called when button is held down.  
# prints goodbye, invokes shutdown process.
def hold():
  GPIO.output(ledPin, GPIO.HIGH)
  printer.println('Goodbye!')
  printer.feed(3)
  subprocess.call("sync")
  subprocess.call(["shutdown", "-h", "now"])
  GPIO.output(ledPin, GPIO.LOW)

# Initialization

# Use Broadcom pin numbers (not Raspberry Pi pin numbers) for GPIO
GPIO.setmode(GPIO.BCM)

# Enable LED and button (w/pull-up on latter)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LED on while working
GPIO.output(ledPin, GPIO.HIGH)

# Processor load is heavy at startup; wait a moment to avoid
# stalling during greeting.
time.sleep(30)

# Print greeting
printer.println('Hello!')
printer.println('Ready to print FFA.')
printer.feed(3)
GPIO.output(ledPin, GPIO.LOW)

# Poll initial button state and time
prevButtonState = GPIO.input(buttonPin)
prevTime        = time.time()
tapEnable       = False
holdEnable      = False

# Main loop
while(True):

  # Poll current button state and time
  buttonState = GPIO.input(buttonPin)
  t           = time.time()

  # Has button state changed?
  if buttonState != prevButtonState:
    prevButtonState = buttonState   # Yes, save new state/time
    prevTime        = t
  else:                             # Button state unchanged
    if (t - prevTime) >= holdTime:  # Button held more than 'holdTime'?
      # Yes it has.  Is the hold action as-yet untriggered?
      if holdEnable == True:        # Yep!
        hold()                      # Perform hold action (usu. shutdown)
        holdEnable = False          # 1 shot...don't repeat hold action
        tapEnable  = False          # Don't do tap action on release
    elif (t - prevTime) >= tapTime: # Not holdTime.  tapTime elapsed?
      # Yes.  Debounced press or release...
      if buttonState == True:       # Button released?
        if tapEnable == True:       # Ignore if prior hold()
          tap()                     # Tap triggered (button released)
          tapEnable  = False        # Disable tap and hold
          holdEnable = False
      else:                         # Button pressed
        tapEnable  = True           # Enable tap and hold actions
        holdEnable = True

  # LED blinks while idle, for a brief interval every 2 seconds.
  # Pin 18 is PWM-capable and a "sleep throb" would be nice, but
  # the PWM-related library is a hassle for average users to install
  # right now.  Might return to this later when it's more accessible.
  if ((int(t) & 1) == 0) and ((t - int(t)) < 0.15):
    GPIO.output(ledPin, GPIO.HIGH)
  else:
    GPIO.output(ledPin, GPIO.LOW)
    

