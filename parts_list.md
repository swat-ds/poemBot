# poemBot Parts list

## Core

> This is a headless Raspberry Pi project. We use Pi 2, but any version should work (note differences in pin layout). Since it is very simple and offline, Pi Zero would work well if you are attempting to run off battery and minimize size. 

- Raspberry Pi 2, https://www.adafruit.com/products/2358 
- SD card 4GB, (install [Raspbian Jessie Lite](https://www.raspberrypi.org/downloads/raspbian/))
- Mini thermal receipt printer, https://www.adafruit.com/products/597
- Thermal paper rolls, https://www.adafruit.com/products/599 (bulk boxes can be found on Amazon)
- Momentary Pushbutton with LED Ring, https://www.adafruit.com/products/558

## Squid style wiring

> To simplify assembly and modification, we use jumper wires soldered to the components, inspired by [simonmonk's Squid](https://github.com/simonmonk/squid). 

- jumper wire, https://www.adafruit.com/products/266 
- Heat shrink, https://www.adafruit.com/products/1649 

## Power

> The printer draws a lot of current when printing, so you need a decent 5V power supply. It should probably deliver more than 3A to ensure the Pi doesn't have brown outs while the printer draws current.

- 5V 10A switching power supply, https://www.adafruit.com/products/658 
- Panel Mount 2.1mm DC barrel jack, https://www.adafruit.com/products/610 

## Handy

> A serial cable is often handy for setting up headless Pi. However, it's not necessary if you ssh or simply directly write on the SD card from linux.

- USB to TTL Serial Cable, https://www.adafruit.com/products/954 

> *Note:* This basically follows [Adafruit IoT Printer project](https://learn.adafruit.com/pi-thermal-printer/parts). However, poemBot is offline since it travels a lot and doesn't need the internet. Furthermore, I suggest not using the T-Cobbler and building your own unique case.
