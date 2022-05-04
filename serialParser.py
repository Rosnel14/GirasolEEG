import serial
import time

#for RPi /dev/ttyACM0 for serial path
#for MacOS /dev/cu.usbmodem00001
ser = serial.Serial('/dev/cu.usbmodem00001',9600)

#this object manages serial communication between
#arduino and RPi

#format for serial communication
#signal strength, attention, meditation, delta, theta, low alpha, high alpha, low beta, high beta, low gamma, high gamma


#seperates string from Arduino


#returns attention value
#for a duration in seconds(int)
def getAttention(duration):
    startTime = time.time()
    while (startTime <= duration):
        read_serial=ser.readline()
        mylist = read_serial.split(b",")
    return mylist



#returns concentration value
def getConcentration():
