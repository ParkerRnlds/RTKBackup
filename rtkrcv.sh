!#/bin/sh
./rtkrcv.exp
cp /home/pi/Documents/RTKBackup/rtklib2.4.2/app/rtkrcv/gcc/rover1.log /home/pi/Documents/RTKBackup/rover.log
sed -n 39p rover.log > location.txt
exit 0