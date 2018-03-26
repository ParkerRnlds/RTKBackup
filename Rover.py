import math
import serial

##initialize serial ports
xbee = serial.Serial('/dev/ttyUSB0', 9600, timeout = .5)
controller = serial.Serial('dev/serial0', 9600, timeout = .5)

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
def calculateBearing(lambdaOne, lambdaTwo sigmaOne, sigmaTwo, dist, radius):
    y = math.sin(lambdaTwo-lambdaOne)*math.cos(sigmaTwo)
    x = math.cos(sigmaOne)*math.sin(sigmaTwo)-math.sin(sigmaOne)*math.cos(sigmaTwo)*math.cos(lambdaTwo-lambdaOne)
    initBearing = math.degrees(math.atan2(y,x))
    return math.asin(math.sin(sigmaOne)*math.cos(dist/radius)+math.cos(sigmaOne)*math.sin(dist/radius)*math.cos(initBearing))

##Get LatLon data
def getDestination():
    d = ""
    while d == "":
        d = ser.readline()
        if d != "":
            break
    return d

##define constants
LeftMotorForward = 0x0

##get in current latitude
latRover = 0.00
##get in current longitude
lonRover = 0.00

##Assuming latitude and longitute are in destination separated by space
    ##i.e. "3.456 4.567"
destination = ""
while destination != "exit":
    destination = getDestination()
    if destination == "exit":
        break
    latLon = destination.split()


##get in destination latitude
latDest = 0.00
##get in destination longitude
lonDest = 0.00

##variables needed for distance/bearing formulas
R = 6371000 ##earth's radius
sigma1 = math.radians(latRover)
sigma2 = math.radians(latDest)
lambda1 = math.radians(lonRover)
lambda2 = math.radians(lonDest)
diffLat = math.radians(latDest - latRover)
diffLon = math.radians(lonDest - lonRover)

##calculate distance
distance = calculateDistance(diffLat, diffLon, sigma1, sigma2, R)

##calculate bearing
bearing = calculateBearing(lambda1, lambda2, sigma1, sigma2, distance, R)

##Add code for turning and driving a certain distance


