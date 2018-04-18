import sys
import serial
import subprocess
import math

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

print(str(latitude))
print(str(longitude))
f.close()
#for x in contents:
    ##parse the data