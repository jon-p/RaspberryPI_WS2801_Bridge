RaspberryPI WS2801 XMAS light effects
=====================================

Forked from the Hackerspaceshop RaspberryPI_WS2801_Bridge (product no longer exists).

/pcb  folder includes latest schematic and baord file (eagle)  + pdf
​
/software/xmas.py cycles through a number of different christmasey effects:
- an all white flickering effect (all pixels white with some flickering on/off).
- a white/blue "rain" effect, with all pixels off and random pixels lighting up in blue or white and fading out.
- a rainbow colour-cycling effect.
- travelling sinewave intesity effect, in white and multicoloured
​
Effects change every 5 minutes via a random transition, one of:
- fading to black.
- wiping to black from the edges.

Run ./install.sh to isntall a startup script that will automatically run xmas.py on boot.

Jon


-----------------8<----------------


Original hackerspace readme
===========================

this is the blinkenpi project

it implements a WS2801 blinken interface for the raspberry pi 2 ws2801 bridge found here: http://www.hackerspaceshop.com/raspberrypi-things/raspberrypi-ws2801.html


the hardware SPI is used and we need py-spidev for that.
a compiled spidev.so is included in this folder.

you can compile your own libraries for spidev if you like to. 
we found the sources here:

https://github.com/doceme/py-spidev
thanks doceme!

have fun!
-flo
