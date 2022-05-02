import serial
import time
#for RPi /dev/ttyACM0 for serial path
#for MacOS /dev/cu.usbmodem00001

ser = serial.Serial('/dev/cu.usbmodem00001',9600)

duration = 5

while (True):
    read_serial=ser.readline()

    #using the byte modifier works!
    mylist = read_serial.split(b",")

    #here I'm getting used to byte type objects
    print(mylist[0] > mylist[1])
