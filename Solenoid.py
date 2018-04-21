#Import the necessary libraries
import RPi.GPIO as GPIO
import time
import serial
import sys
#initialize Xbee
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = .5)

GPIO.setmode(GPIO.BCM)
#Setup pin 18 as an output
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
#This function turns the valve on and off in 10 sec. intervals. 
def valve_OnOff(Pin):
        GPIO.output(Pin, GPIO.HIGH)
        print("GPIO HIGH (on), valve should be on") 
        time.sleep(30) #waiting time in seconds
        GPIO.output(Pin, GPIO.LOW)
        print("GPIO LOW (off), valve should be off")
        
while True:
    data_fresh = ser.readline()
    if data_fresh == "here"
        valve_OnOff(18)
        
    
GPIO.cleanup()