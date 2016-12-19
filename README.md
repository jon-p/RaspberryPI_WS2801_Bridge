RaspberryPI WS2801 XMAS light effects
=====================================

Forked from the Hackerspaceshop RaspberryPI_WS2801_Bridge (product no longer exists).

/pcb  folder includes latest schematic and baord file (eagle)  + pdf
/software includes all the raspberry pi software
/image contains one big image file that you can directly dd to an SD card (min 4GB)

/software/xmas.py cycles through a number of different christmasey effects:
- an all white flickering effect (all pixels white with some flickering on/off).
- a white/blue "rain" effect, with all pixels off and random pixels lighting up in blue or white and fading out.
- a rainbow colour-cycling effect.
- travelling sinewave intesity effect, in white and multicoloured.

Effects change every 5 minutes via a random transition, one of:
- fading to black.
- wiping to black from the edges.

