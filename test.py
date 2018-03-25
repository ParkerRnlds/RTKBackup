##import serial
##import sys
##ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = .5)
##
##while True:
##    serialcmd = sys.stdout
##    #ser.write(serialcmd.encode())
##    #data_fresh = ser.readline()
##    #print (data_fresh)
##    print (serialcmd)

import serial
import time

s = serial.Serial("/dev/serial0", 9600, timeout=0.5)

def sendCommand(cmd1, cmd2):
    cmd = (chr(0xAA) + chr(0x0A) + chr(cmd1) + chr(cmd2)).encode()
    command = cmd.split(b'\xc2', 1)
    s.write(command[1])


sendCommand(0x08, 0x7F) #motor 0 reverse
sendCommand(0x0E, 0x7F) #motor 1 reverse
time.sleep(5)
sendCommand(0x08, 0x00) #motor 0 stop
sendCommand(0x0E, 0x00) #motor 1 stop

s.close()

