#!/usr/bin/python
# prints random poem from collection 
# designed for headless Raspberry Pi connected to thermal printer 
# called from a main script when print button is pressed

from __future__ import print_function
from thermalPrinter import *
import random

# printer set up 
printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

# set up content for print outs
website = "poetry.lib.uidaho.edu"
publisher = "Copper Canyon Press"

# set up poems in list of lists
# or import from a csv and create list 
poems = [["Title", "Author", """Poem""", "Book", "VPOD Date"],[etc]]

#get a random poem
randPoem = random.choice(poems)

# nicely wrap the content for the printer
# Title and Author are printed in 'M' medium font, limit is 32 character per line
# poem is printed in 'S' small font, limit is 32 characters per line 
# book and publisher are in "fontB", limit is 42 character per line 
wrappedTitle = textwrap.fill(randPoem[0], width=32)
wrappedAuthor = textwrap.fill("    by " + randPoem[1], width=32, subsequent_indent="    ")
wrappedBook = textwrap.fill("    from: " + randPoem[3], width=42, subsequent_indent="    ")
wrappedPoem = ""
for line in randPoem[2].splitlines():
    wrappedLine = textwrap.fill(line, width=32, subsequent_indent="    ")
    wrappedPoem += wrappedLine +"\n"
#print the poem on the thermal printer
printer.justify('L')
printer.setSize('M')
printer.println(wrappedTitle + "\n" + wrappedAuthor)
printer.setSize('S')
printer.println(wrappedPoem)
printer.println(' ')
printer.writeBytes(0x1B, 0x21, 0x1)
printer.println(wrappedBook + "\n" + publisher)
printer.setSize('S')
printer.println(' ')
printer.justify('C')
printer.println("VPOD " + randPoem[4])
printer.println(website)
printer.println(' ')
printer.println(' ')
printer.feed(4)


