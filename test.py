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
##import serial
##import sys
##import time
##while True:
##    serialcmd = chr(0xAA) + chr(0x09) + chr(0x0A) + chr(0x7F)##
##    print("this shit is not working1")
##    s = serial.Serial("/dev/serial0", 9600, timeout=0.5)
##    print("this shit is not working2")
##    time.sleep(2)
##    print("this shit is not working3")
##    s.write(serialcmd.encode())##  )    # motor 0 full speed reverse
##    print(serialcmd)
##    
####s.write( chr(0xAA) )##+ chr(0x09) + chr(0x0A) + chr(0x00) )      # motor 0 stop
##s.close()
import serial
import time

s = serial.Serial("/dev/serial0", 38400, timeout=0.5)
time.sleep(2)

s.write( chr(0xAA) + chr(0x0A) + chr(0x0A) + chr(0x7F) )    # motor 0 full speed reverse


time.sleep(2)    
s.write( chr(0xAA) + chr(0x0A) + chr(0x0A) + chr(0x00) )      # motor 0 stop
s.close()
