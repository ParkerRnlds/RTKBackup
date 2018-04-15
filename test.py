import serial
import sys
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = .5)

while True:
    serialcmd = sys.stdout
    ser.write(serialcmd.encode())
    data_fresh = ser.readline()
    print (data_fresh)
    print (serialcmd)
