Original repo readme below.

Run install.sh to isntall a startup script that will automatically run xmas.py on boot.

xmas.py runs through a series of Christmasey animations/effects fot WS2801 based lights.

--------------8<------------

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


