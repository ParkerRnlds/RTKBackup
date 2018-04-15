import serial
import sys
import time
from dual_mc33926_rpi import motors

xbee = serial.Serial('/dev/ttyUSB0', 9600, timeout = .5)
serialcmd = "30.420033 -84.317676" #input("Enter Destination: ")

while True:
    motors.enable()
    #motors.motor2.setSpeed(480)
    time.sleep(2)
    #motors.motor2.setSpeed(0)
    #xbee.write(serialcmd.encode())
    ##time.sleep(1)
    #print (serialcmd)