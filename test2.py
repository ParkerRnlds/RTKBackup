import serial
import sys
import time
def sendCommand(cmd1, cmd2):
    cmd = (chr(0xAA) + chr(0x0A) + chr(cmd1) + chr(cmd2)).encode()
    command = cmd.split(b'\xc2', 1)
    s.write(command[1])


sendCommand(0x08, 0x6F) #motor 0 reverse
sendCommand(0x0E, 0x6F) #motor 1 reverse
time.sleep(5)
sendCommand(0x08, 0x00) #motor 0 stop
sendCommand(0x0E, 0x00) #motor 1 stop

s.close()