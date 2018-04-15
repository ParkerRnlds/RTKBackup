import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

try:
    GPIO.output(4, 1)
    GPIO.output(2, 1)
    print("GPIO HIGH (on)")
    GPIO.output(3, 1)
    time.sleep(3)
    GPIO.output(2, 0)
    GPIO.output(3, 0)
    GPIO.output(4, 0)
    print("GPIO HIGH (off)")
except KeyboardInterrupt:
    GPIO.cleanup()