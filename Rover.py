#!/usr/bin/python

import math
import serial
import time

##initialize serial ports
#xbee = serial.Serial('/dev/ttyUSB0', 9600, timeout = .5)
controller = serial.Serial('/dev/serial0', 9600, timeout = .5)

##Sends command to motor controller
def sendCommand(cmd1, cmd2):
    cmd = (chr(0xAA) + chr(0x0A) + chr(cmd1) + chr(cmd2)).encode()
    command = cmd.split(b'\xc2', 1)
    controller.write(command[1])

##Calculate distance between 2 points
def calculateDistance(deltaLat, deltaLon, sigmaOne, sigmaTwo, radius):
    a = math.sin(deltaLat/2)*math.sin(deltaLat/2)+math.cos(sigmaOne)*math.cos(sigmaTwo)*math.sin(deltaLon/2)*math.sin(deltaLon/2)
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    return radius * c;

##Calculate bearing needed to turn to
def calculateBearing(lambdaOne, lambdaTwo, sigmaOne, sigmaTwo, dist, radius):
    y = math.sin(lambdaTwo-lambdaOne)*math.cos(sigmaTwo)
    x = math.cos(sigmaOne)*math.sin(sigmaTwo)-math.sin(sigmaOne)*math.cos(sigmaTwo)*math.cos(lambdaTwo-lambdaOne)
    initBearing = math.degrees(math.atan2(y,x))
    return math.asin(math.sin(sigmaOne)*math.cos(dist/radius)+math.cos(sigmaOne)*math.sin(dist/radius)*math.cos(initBearing))

##Get destination LatLon data
def getDestination():
    line = ser.readline().strip()
    d = line.decode()
    while d == "":
        line = ser.readline().strip()
        d = line.decode()
        if d != "":
            break
    return d

##get current location LatLon data
def getLocation():
    f = open("Rover.log", "r")
    contents = f.readlines()
    f.close()
    for x in contents:
        ##parse the data
    f.close()

##Motor Commands
def turnLeft(seconds):
	sendCommand(leftForward, fullSpeed)
	time.sleep(seconds)
	sendCommand(leftForward, zeroSpeed)
	
def turnRight(seconds):
	sendCommand(rightForward, fullSpeed)
	time.sleep(seconds)
	sendCommand(rightForward, zeroSpeed)
	
def fullSpeedAhead(seconds):
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
	
def readCompass():
    f = open("compassresult.txt", "r")
    contents = f.readlines()
    for x in contents:
        tempList = x.split()
        if (tempList != []):
            if (tempList[0] == "heading"):
                direction = tempList[1]
    f.close()
    return direction

##define constants
leftForward = 0x08
leftReverse = 0x0A
rightForward = 0x0C
rightReverse = 0x0E

fullSpeed = 0x7F
zeroSpeed = 0x00

##get in current latitude
latRover = 0.00
##get in current longitude
lonRover = 0.00

##Assuming latitude and longitute are in destination separated by space
    ##i.e. "3.456 4.567", reads in destination latitude and longitude
destination = getDestination()
while destination != "exit":
    destination = getDestination()
    if destination == "exit":
        break
    latLon = destination.split()
    latDest = latLon[0]
    lonDest = latLon[1]

    location = getLocation()
    
    variables needed for distance/bearing formulas
    R = 6371000 ##earth's radius
    sigma1 = math.radians(latRover)
    sigma2 = math.radians(latDest)
    lambda1 = math.radians(lonRover)
    lambda2 = math.radians(lonDest)
    diffLat = math.radians(latDest - latRover)
    diffLon = math.radians(lonDest - lonRover)

    calculate distance
    distance = calculateDistance(diffLat, diffLon, sigma1, sigma2, R)

    calculate bearing
    bearing = calculateBearing(lambda1, lambda2, sigma1, sigma2, distance, R)

    Add code for turning and driving a certain distance
fullSpeedAhead(5)
sendCommand(leftForward, fullSpeed)
time.sleep(10)
sendCommand(leftForward, zeroSpeed)
	

p