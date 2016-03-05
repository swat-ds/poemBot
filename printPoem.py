#!/usr/bin/python

from __future__ import print_function
from Adafruit_Thermal import *
import random

# printer set up 
printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

# set up content for print outs
website = "poetry.lib.uidaho.edu"
publisher = "Copper Canyon Press"

#set up poems in list of lists
poems = [["Title", "Author", """Poem""", "Book", "VPOD Date"],[etc]]

#get a random poem
randPoem = random.randrange(0,len(poems)+1)

#print the poem on the thermal printer
printer.justify('L')
printer.setSize('M')
printer.println(poems[randPoem][0] + "\n" + poems[randPoem][1])
printer.setSize('S')
printer.println(poems[randPoem][2])
printer.println(' ')
printer.writeBytes(0x1B, 0x21, 0x1)
printer.println(poems[randPoem][3] + "\n" + publisher)
printer.setSize('S')
printer.println(' ')
printer.justify('C')
printer.println("VPOD: " + poems[randPoem][4])
printer.println(website)
printer.println(' ')
printer.println(' ')
printer.feed(4)


