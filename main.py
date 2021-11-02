#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This code was extracted from the pimoroni breakout-garden autodetect.py file :
https://github.com/pimoroni/breakout-garden/blob/master/autodetect.py
"""
import smbus2
import sys

I2C_BUS = 1

try:
    bus = smbus2.SMBus(I2C_BUS)
    bus.close()
    print('')
    print("Seems like smbus access didn't raised any error...")
    print('')
    print('¯\_(ツ)_/¯ github.com/promethee ¯\_(ツ)_/¯')
except IOError:
    print("Unable to access /dev/i2c-{}, please ensure i2c is enabled!".format(I2C_BUS))
    sys.exit()
