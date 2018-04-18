#!/usr/bin/python3

import serial
import time

s = serial.Serial('/dev/ttyUSB0', 9600, timeout = .5)
while True:
    line = s.readline()
    print(line)