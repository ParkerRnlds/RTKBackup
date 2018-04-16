import serial
import sys
import time
#from dual_mc33926_rpi import motors

xbee = serial.Serial('/dev/ttyUSB0', 9600, timeout = .5)
serialcmd = "30.420033 -84.317676" #input("Enter Destination: ")
def getLocations():
    choice = "n"
    while choice != "y" and choice != "Y":
        a = input("\nEnter destinations separated by comma.\ni.e. 1.23 4.56,7.89 10.11: ")
        locations = a.split(',')
        print("\nThe Rover will travel to: ")
        for i in range(0, len(locations)):
            print(locations[i])
        choice = input("\nIs this correct? [y/n]")
        
    a = a + ",exit\r"
    return a

locations = getLocations()
serialcmd = locations
##    print("\nSending next command..")
xbee.write(serialcmd.encode())
##    #receivedData = xbee.read(xbee.inWaiting())
##    #print("\nReceived: ")
##    print(receivedData)
##    if serialcmd != "exit":
##        print("\nRobot is traveling to next location")
##        ##motors.motor2.enable()
##        ##motors.motor2.setSpeed(480)
##        ##time.sleep(2) 
##        ##motors.motor2.setSpeed(0)
##        ##time.sleep(1)
##        ##print (serialcmd)
##    else:
##        print("\nExit command sent. Your lawn is now watered")
##        break
