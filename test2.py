import serial
import sys
import time
while True:
    serialcmd = chr(0xAA) + chr(0x0A) + chr(0x0A) + chr(0x7F)##
    print("this shit IS working1")
    s = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
    print("this shit is not working2")
    time.sleep(2)
    print("this shit is not working3")
    s.write(bytes(serialcmd, 'latin-1'))##  )    # motor 0 full speed reverse
    print(serialcmd)
    
##s.write( chr(0xAA) )##+ chr(0x09) + chr(0x0A) + chr(0x00) )      # motor 0 stop
s.close()