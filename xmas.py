# Xmas pixel effects
# 2015 Jon Payne (jon-p on github)
#
# Derived from this work (thanks!):
#
# Simple Example for accessing WS2801 LED stripes
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

import math
import sys
import time
import random

from LedStrip_WS2801 import LedStrip_WS2801




def mySin(a, min, max):
    return min + ((max - min) / 2.) * (math.sin(a) + 1)

class rainbow:
    def __init__(self, led, sleep):
        self.t = 0
        self.led = led
        self.sleep = sleep

    def generateColour(self, a):
        intense = 255
        return [int(mySin(a, 0, intense)), 
                int(mySin(a + math.pi / 2, 0, intense)), 
                int(mySin(a + math.pi, 0, intense))]

    def execute(self):
        self.t = self.t + 1
        for i in range(0, self.led.nLeds):
            self.led.setPixel(i, self.generateColour((1.1 * math.pi * (i*2 + self.t)) / self.led.nLeds))
        self.led.update()
        if (self.sleep != 0):
            time.sleep(self.sleep)

def anyLit(ledStrip):
    a = 0
    for i in range(0,ledStrip.nLeds):  
        pixel = ledStrip.getPixel(i)
        a += pixel[0] + pixel[1] + pixel[2]
    return int(a) > 0

def fadeToBlack(ledStrip):
    while (anyLit(ledStrip)):
        ledStrip.multAll(0.9)
        ledStrip.update()
        time.sleep(0.01)

class sinewave:
    def __init__(self, led):
        self.theta = 0.0
        self.led = led

    def monochrome(self):
        self.theta = self.theta + 0.01
        beta = 0.0
        for p in range (0, self.led.nLeds):
            beta = beta + 0.5
            a = mySin(beta + self.theta, 0.0, 255.0)
            self.led.setPixel(p, (a,a,a) )
        self.led.update()

    def multiColour(self):
        self.theta = self.theta + 0.025
        theta = self.theta
        beta = 0.0
        maxR = mySin(theta * -0.7, 0.0, 255.0)
        maxG = mySin(theta * 0.4, 0.0, 255.0)
        maxB = mySin((theta * 0.5) + (math.pi /2.0), 0.0, 255.0)
        for p in range (0, self.led.nLeds):
            beta = beta + 0.5
            #dR = beta + theta
            #dG = beta + (theta *2.3) 
            #dB = beta + (theta *1.7) + (math.pi)
            dR = beta + theta
            dG = (beta *1.9) + theta
            dB = (beta *0.3) + theta
            r = mySin(dR, 0.0, maxR)
            g = mySin(dG, 0.0, maxG)
            b = mySin(dB, 0.0, maxB)
            self.led.setPixel(p, (r,g,b) )
        self.led.update()


def plinkWhite():
    return [255,255,255]

def plinkRandom():
    return [random.randint(1,255), random.randint(1,255), random.randint(1,255)]

xmasColours1 = [ [155,155,155], [0,0,255], [50,50,200], [0,0,200] ]
def plinkXmas():
    return xmasColours1[ random.randint(0,len(xmasColours1)-1) ]

class plink:
    def __init__(self, ledStrip, colourFunc):
        self.led = ledStrip
        self.setRand = 5
        self.colourFunc = colourFunc

    def findBlackPixelIdx(self):   
        maxPixel = self.led.getNumPixels() - 1
        i = random.randint(0,maxPixel)
        while (self.led.getIntPixel(i) != [0,0,0]):
            i = random.randint(0,maxPixel)
        return i

    def execute(self):
        self.led.multAll(0.95)
        if (random.randint(1, self.setRand) == 1):
            self.led.setPixel( self.findBlackPixelIdx(), self.colourFunc())
        self.led.update()
        time.sleep(0.01)


class flicker:
    def __init__(self, ledStrip):
        self.led = ledStrip

    def fill(self, color, start, skip):
        a = random.randint(25,255)
        for i in range(start, ledStrip.nLeds, skip):
            r = random.randint(a,255)
            self.led.setPixel(i, [int(color[0] / 255.0 * r), int(color[1] / 255.0 * r), int(color[2] / 255.0 * r)])

    def execute(self):
        time.sleep(0.007 * random.randint(1,15))
        self.fill( [255,255,255], 0, 5)
        self.fill( [255,255,255], 1, 5)
        self.fill( [255,0,0], 2, 5)
        self.fill( [255,0,0], 3, 5)
        self.fill( [0,255,0], 4, 5)
        self.led.update()


def wipe(ledStrip):
    r= 0
    mid = int(math.ceil(ledStrip.nLeds / 2.0))
    for i in range(0, mid):
        ledStrip.setPixel(i, [r,r,r])
        ledStrip.setPixel(ledStrip.nLeds - 1 -i, [r,r,r])
        ledStrip.update()
        time.sleep(0.05)
    time.sleep(1.0)

def transition(ledStrip):
  transitions = [
    lambda: wipe(ledStrip),
    lambda: fadeToBlack(ledStrip)
    ]
  transition = transitions[random.randint(0,len(transitions)-1)]
  transition()



def run(durationSecs, func):
    endTime = time.time() + durationSecs
    while (time.time() < endTime):
        func()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        nrOfleds = 47
    else:
        nrOfleds = int(sys.argv[1])
    delayTime = 0.01

    ledStrip = LedStrip_WS2801(nrOfleds)
    ledStrip.setAll([0,0,0])
    ledStrip.update()
    time.sleep(1.0)
    
    effects = [
        plink(ledStrip, plinkXmas).execute,
        sinewave(ledStrip).multiColour,
	flicker(ledStrip).execute,
        rainbow(ledStrip, 0.05).execute,
        sinewave(ledStrip).monochrome
	]

    durationSecs = 5.0 * 60.0

    try:
        func = 0
        while 1:       
            effect = effects[func % len(effects)]
            run(durationSecs, effect)
            func = func + 1
            transition(ledStrip)
    except KeyboardInterrupt:
        fadeToBlack(ledStrip)
        ledStrip.close()

