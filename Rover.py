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
    for i in range (0, len(commands) - 1):
        tempList = list(commands[i])
        for j in range (0, len(tempList) - 1):
            if tempList[j] == ':':
                tempList[j] = ' '
        commands[i] = ''.join(tempList)
    print("\nNew commands: \n")
    for i in range(0, len(commands)):
        print(commands[i])
    return commands

#get current location LatLon data
def getLocation():
    longitudeNegative = False
    latitudeNegative = False

    print("\nReading current location...\n")
    f = open("test.txt", "r")
    contents = f.readlines()
    locationList = contents[0].split(',')
    latitudeDMS = locationList[2]
    print(latitudeDMS)
    longitudeDMS = locationList[4]
    print(longitudeDMS)
    if longitudeDMS[0] == '0':
        longitudeNegative = True
        temp = list(longitudeDMS)
        temp[0] = '-'
        longitudeDMS = ''.join(temp)
    if latitudeDMS[0] == '0':
        latitudeNegative = True
        temp = list(latitudeDMS)
        temp[0] = '-'
        latitudeDMS = ''.join(temp)
        
    if latitudeNegative == True:
        latDeg = latitudeDMS[0] + latitudeDMS[1] + latitudeDMS[2]
        latMin = latitudeDMS[3] + latitudeDMS[4] + latitudeDS[5] + latitudeDMS[6] + latitudeDMS[7] + latitudeDMS[8] + latitudeDMS[9] + latitudeDMS[10]
    else:
        latDeg = latitudeDMS[0] + latitudeDMS[1]
        latMin = latitudeDMS[2] + latitudeDMS[3] + latitudeDMS[4] + latitudeDMS[5] + latitudeDMS[6] + latitudeDMS[7] + latitudeDMS[8] + latitudeDMS[9]
        
    if longitudeNegative == True:
        lonDeg = longitudeDMS[0] + longitudeDMS[1] + longitudeDMS[2]
        lonMin = longitudeDMS[3] + longitudeDMS[4] + longitudeDMS[5] + longitudeDMS[6] + longitudeDMS[7] + longitudeDMS[8] + longitudeDMS[9] + longitudeDMS[10]
    else:
        lonDeg = longitudeDMS[0] + longitudeDMS[1]
        lonMin = longitudeDMS[2] + longitudeDMS[3] + longitudeDMS[4] + longitudeDMS[5] + longitudeDMS[6] + longitudeDMS[7] + longitudeDMS[8] + longitudeDMS[9]
        
    latDeg = float(latDeg.strip())
    latMin = float(latMin.strip())
    lonDeg = float(lonDeg.strip())
    lonMin = float(lonMin.strip())

    latitude = math.fabs(latDeg) + math.fabs(latMin/60)
    if latitudeNegative == True:
        latitude = latitude * -1
    longitude = math.fabs(lonDeg) + math.fabs(lonMin/60)
    if longitudeNegative == True:
        longitude = longitude * -1

    location = str(latitude) + " " + str(longitude)
    f.close()
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

#Assuming latitude and longitude are in destination separated by space
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
	
