# poemBot

> printer + pi + python + poems. 

> A Raspberry Pi connected to a thermal printer offers physical prints from a daily poetry website, http://poetry.lib.uidaho.edu/

Easy to read, carry in your pocket, and share with your friends-- poems printed on receipts are fun!

Here is a little video: https://twitter.com/VandalPoem/status/704377485593432065 

Based on Adafruit IoT Printer, https://learn.adafruit.com/pi-thermal-printer/overview

Uses printer library from Adafruit Python-Thermal-Printer, https://github.com/adafruit/Python-Thermal-Printer/blob/master/Adafruit_Thermal.py

We currently use version 2, vpodMainV2.py

# Prepare Poems

The printer script loads the poems from a CSV with the columns: VPODdate, title, author, poem, book.
VPODdate is the date the poem appeared as Poem of the Day. 
The poem column contains the full text of the poem with no markup, only \n.
The book column is the title of the book where the poem appears and year of publication.

I exported all poems from the poetry website in XML, with embedded HTML markup. 
I used [OpenRefine](https://github.com/OpenRefine/OpenRefine) to parse the XML and transform the data. 
I cleaned up the HTML markup, replacing CSS indentation with spaces and adding \n. 

Since the thermal printer is small with 32 normal characters per line, larger poems could take several feet of paper to print. 
I decided to limit the pool of poems based on number of lines and total characters. 
This can be done quickly with OpenRefine by creating new columns based on poem with ```value.split("\n").length()``` and ```length(value)```,
then adding numeric facets. Export the subset of poems data as CSV from OpenRefine. 

Edit the CSV to remove the header and check the character encoding to avoid issues with Python and the printer.

# Set Up

After setting up and testing the Python main loop and poem printing, set it to load on boot by editing rc.local:

```sudo nano /etc/rc.local```

Add the terminal command to start the python script before the line "exit 0":

```
cd /home/pi/Python-Thermal-Printer
python vpodMainV2.py &
```

# References

UBC RAD-device, https://github.com/asistubc/RAD-device

Little Box of Poems, http://www.suppertime.co.uk/blogmywiki/2012/12/pi-poems/

Adafruit IoT Printer, https://learn.adafruit.com/pi-thermal-printer/overview

