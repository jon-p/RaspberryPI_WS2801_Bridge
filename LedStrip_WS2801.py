# Simple Python Library for accessing WS2801 LED stripes
# Copyright (C) 2013  Philipp Tiefenbacher <wizards23@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# For more information about this project please visit:
# http://www.hackerspaceshop.com/ledstrips/raspberrypi-ws2801.html

import spidev






class LedStrip_WS2801(object):
    """Access to SPI with python spidev library."""
    # spiDevice has format [
    def __init__(self, nLeds, nBuffers=1):
        self.spi = spidev.SpiDev()  # create spi object
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 1000000
        self.nLeds = nLeds
        self.nBuffers = nBuffers
        self.buffers = []
        for i in range(0, nBuffers):
            ba = []
            for l in range(0, nLeds):
                ba.extend([0.0, 0.0, 0.0])
            self.buffers.append(ba)
        
        self.gamma = bytearray(256)
        for i in range(256):
	    self.gamma[i] = int(pow(float(i) / 255.0, 2.5) * 255.0 + 0.5)
 

    def close(self):
        if (self.spi != None):
            self.spi.close()
            self.spi = None

    def getNumPixels(self):
        return self.nLeds

    def update(self, bufferNr=0):
        buf = self.buffers[bufferNr]
        ba = []
        for index in range(0,self.nLeds):
            v = buf[index*3: index*3+3]
            ba.extend( [int(v[0]), int(v[1]), int(v[2])] )
        self.spi.writebytes(ba)

    def multAll(self, mult, bufferNr=0):
	for index in range(0, self.nLeds):
            v = self.getPixel(index, bufferNr)
            self.setPixel(index, (v[0] * mult, v[1] * mult, v[2] * mult), bufferNr)

    def subtractAll(self, amount, bufferNr=0):
	for index in range(0, self.nLeds):
            v = self.getPixel(index, bufferNr)
            n = (max(0.0, v[0] - amount), max(0.0, v[1] - amount), max(0.0, v[2] - amount))
            self.setPixel(index, n, bufferNr)
       
    def getPixel(self, index, bufferNr=0):
        return self.buffers[bufferNr][index*3:index*3+3]

    def getIntPixel(self, index, bufferNr=0):
        fp = self.getPixel(index, bufferNr)
        return [int(fp[0]), int(fp[1]), int(fp[2])]

    def setAll(self, color, bufferNr=0):
        for i in range(0, self.nLeds):
            self.setPixel(i, color, bufferNr)

    def setPixel(self, index, color, bufferNr=0):
        self.buffers[bufferNr][index * 3:index * 3 + 3] = color


