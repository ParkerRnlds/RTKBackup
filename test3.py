import sys
import serial
import subprocess

print("\nReading current location...\n")
#subprocess.call(['sudo', './rtkrcv.sh'])
f = open("test.txt", "r")
contents = f.readlines()
for i in contents:
    print(i)
f.close()
#for x in contents:
    ##parse the data