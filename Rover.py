include math
include serial

##set serial to XBEE to read in destination lat/lon
s = serial.Serial('/dev/ttyUSB0', 9600, timeout = .5)



##get in current latitude
latRover = 0.00
##get in current longitude
lonRover = 0.00

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

##calculate distance from current point to next point

diffLat = math.radians(latDest - latRover)
diffLon = math.radians(lonDest - lonRover)

a = math.sin(diffLat/2)*math.sin(diffLat/2)+math.cos(sisgma1)*math.cos(sigma2)*math.sin(diffLon/2)*math.sin(diffLon/2)
c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))

distance = R * c;

##calculate initial bearing

y = math.sin(lambda2-lambda1)*math.cos(sigma2)
x = math.cos(sigma1)*math.sin(sigma2)-math.sin(sigma1)*math.cos(sigma2)*math.cos(lambda2-lambda1)

bearing = math.degrees(math.atan2(y,x))

##calculate final bearing

finalBearing = math.asin(math.sin(sigma1)*math.cos(distance/R)+math.cos(sigma1)*math.sin(distance/R)*math.cos(bearing))

##Add code for turning and driving a certain distance