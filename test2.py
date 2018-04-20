import serial
import sys
import time
<<<<<<< HEAD
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
=======
def sendCommand(cmd1, cmd2):
    cmd = (chr(0xAA) + chr(0x0A) + chr(cmd1) + chr(cmd2)).encode()
    command = cmd.split(b'\xc2', 1)
    s.write(command[1])


sendCommand(0x08, 0x6F) #motor 0 reverse
sendCommand(0x0E, 0x6F) #motor 1 reverse
time.sleep(5)
sendCommand(0x08, 0x00) #motor 0 stop
sendCommand(0x0E, 0x00) #motor 1 stop

>>>>>>> origin/master
s.close()