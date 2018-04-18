#!/usr/bin/python3

import serial
import time

test = "3.45:6.78"
temp = list(test)
for i in range (0, len(temp) - 1):
    if temp[i] == ':':
        temp[i] = ' '
final = ''.join(temp)
print(final)