#!/usr/bin/python

import sys
import math
import serial
import time
import subprocess

#initialize serial ports
xbee = serial.Serial('/dev/ttyUSB0', 9600, timeout = .5)
controller = serial.Serial('/dev/serial0', 9600, timeout = .5)

#Sends command to motor controller
def sendCommand(cmd1, cmd2):
    cmd = (chr(0xAA) + chr(0x0A) + chr(cmd1) + chr(cmd2)).encode()
    command = cmd.split(b'\xc2', 1)
    controller.write(command[1])

#Calculate distance between 2 points
def calculateDistance(deltaLat, deltaLon, sigmaOne, sigmaTwo, radius):
    print("\nCalculating distance...\n")
    a = math.sin(deltaLat/2)*math.sin(deltaLat/2)+math.cos(sigmaOne)*math.cos(sigmaTwo)*math.sin(deltaLon/2)*math.sin(deltaLon/2)
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    return radius * c;

#Calculate bearing needed to turn to
def calculateBearing(lambdaOne, lambdaTwo, sigmaOne, sigmaTwo, dist, radius):
    print("\nCalculating bearing...\n")
    y = math.sin(lambdaTwo-lambdaOne)*math.cos(sigmaTwo)
    x = math.cos(sigmaOne)*math.sin(sigmaTwo)-math.sin(sigmaOne)*math.cos(sigmaTwo)*math.cos(lambdaTwo-lambdaOne)
    initBearing = math.degrees(math.atan2(y,x))
    return math.asin(math.sin(sigmaOne)*math.cos(dist/radius)+math.cos(sigmaOne)*math.sin(dist/radius)*math.cos(initBearing))

#Get destination LatLon data
def getDestination():
    print("\nReading destination commands...")
    line = xbee.readline().strip()
    readLine = line.decode()
    commands = readLine.split(',')
    print("\nThese commands received: \n")
    for i in range(0, len(commands) - 1):
        print(commands[i])
    while commands[len(commands) - 1] != "exit":
        line = xbee.readline(xbee.inWaiting()).strip()
        d = line.decode()
        if d != "":
            readLine = readLine + d
            #put space in between
        commands = readLine.split(',')
    print("\nNew commands: \n")
    for i in range(0, len(commands)):
        print(commands[i])
    return commands

#get current location LatLon data
def getLocation():
    print("\nReading current location...\n")
    #subprocess.call(['sudo', './rtkrcv.sh'])
    #f = open("Rover.log", "r")
    #contents = f.readlines()
    #f.close()
    #for x in contents:
        ##parse the data
    #f.close()
    location = "30.4205 -84.3180"
    return location

#Motor Commands
def turnLeft(seconds):
    print("\nTurning left\n")
    sendCommand(leftForward, fullSpeed)
    sendCommand(rightReverse, fullSpeed)
    time.sleep(seconds)
    sendCommand(rightReverse, zeroSpeed)
    sendCommand(leftForward, zeroSpeed)
	
def turnRight(seconds):
    print("\nTurning right\n")
    sendCommand(rightForward, fullSpeed)
    sendCommand(leftReverse, fullSpeed)
    time.sleep(seconds)
    sendCommand(leftReverse, zeroSpeed)
    sendCommand(rightForward, zeroSpeed)
	
def fullSpeedAhead(seconds):
    print("\nShifting into MAXIMUM OVERDRIVE\n")
    sendCommand(leftForward, fullSpeed)
    sendCommand(rightForward, fullSpeed)
    time.sleep(seconds)
    sendCommand(rightForward, zeroSpeed)
    sendCommand(leftForward, zeroSpeed)
	
def reverse(seconds):
    sendCommand(leftReverse, fullSpeed)
    sendCommand(rightReverse, fullSpeed)
    time.sleep(seconds)
    sendCommand(rightReverse, zeroSpeed)
    sendCommand(leftReverse, zeroSpeed)

#Read compass	
def readCompass():
    print("\nGetting current bearing...\n")
    subprocess.call(['sudo', './compass_scr.sh'])
    f = open("compassresult.txt", "r")
    contents = f.readlines()
    for x in contents:
        tempList = x.split()
        if (tempList != []):
            if (tempList[0] == "heading"):
                direction = tempList[1]
    f.close()
    return direction

#define constants
leftForward = 0x0A
leftReverse = 0x08
rightForward = 0x0C
rightReverse = 0x0E

fullSpeed = 0x6F
zeroSpeed = 0x00

#get in current latitude
latRover = 0.00
#get in current longitude
lonRover = 0.00

#Assuming latitude and longitute are in destination separated by space
    #i.e. "3.456 4.567", reads in destination latitude and longitude
print("\nWaiting for commands...\n")
commands = getDestination()
for i in range(0, len(commands) - 1):
    if commands[i] == "exit":
        break
    latLon = commands[i].split()
    latDest = float(latLon[0].strip())
    lonDest = float(latLon[1].strip())
    if i == 0:
        location = getLocation()
    else:
        location = commands[i - 1]
    latLon = location.split()
    latRover = float(latLon[0].strip())
    lonRover = float(latLon[1].strip())
    
    print("\nCurrent latitude and longitude: ")
    print(latRover)
    print(" ")
    print(lonRover)
    print("\nDestination: ")
    print(latDest)
    print(" ")
    print(lonDest)
    
    #variables needed for distance/bearing formulas
    R = 6371000 #earth's radius
    sigma1 = math.radians(latRover)
    sigma2 = math.radians(latDest)
    lambda1 = math.radians(lonRover)
    lambda2 = math.radians(lonDest)
    diffLat = math.radians(latDest - latRover)
    diffLon = math.radians(lonDest - lonRover)
    
    #speed variables
    driveSpeed = 1.4986 #m/s
    turnSpeed = 180 #deg/sec
    
    #calculate distance
    distance = calculateDistance(diffLat, diffLon, sigma1, sigma2, R)
    secondsForward = distance/driveSpeed
    print(secondsForward)
    #calculate bearing
    bearing = calculateBearing(lambda1, lambda2, sigma1, sigma2, distance, R)
    currentBearing = float(readCompass().strip())
    degreesNeeded = currentBearing - bearing;
    secondsToTurn = math.fabs(degreesNeeded)/turnSpeed
    print(secondsToTurn)

    #Go
    print("\nTurning...\n")
    if (degreesNeeded >= 0 and degreesNeeded <= 180):
        turnRight(secondsToTurn)
    else:
        turnLeft(secondsToTurn)
    print("\nDriving...\n")
    fullSpeedAhead(secondsForward)
    print("The dark deed you requested is done, sir")
	
