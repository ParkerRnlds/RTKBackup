import time
from dual_mc33926_rpi import motors, MAX_SPEED

motors.motor2.enable()
motors.motor2.setSpeed(480)
time.sleep(5)
motors.motor2.setSpeed(0)
motors.motor2.disable()