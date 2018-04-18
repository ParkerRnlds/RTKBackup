#!/bin/sh
cd /home/pi/Documents/RTKBackup/rtklib2.4.2/app/rtkrcv/gcc
sudo ./rtkrcv.exp
sudo cp /home/pi/Documents/RTKBackup/rtklib2.4.2/app/rtkrcv/gcc/rover1.log /home/pi/Documents/RTKBackup/rover.log
cd /home/pi/Documents/RTKBackup
sudo sed -n 39p rover.log > location.txt
sudo python3 Rover.py
exit 0