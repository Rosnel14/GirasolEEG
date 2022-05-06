import serial
import time

#for RPi /dev/ttyACM0 for serial path
#for MacOS /dev/cu.usbmodem00001
ser = serial.Serial('/dev/cu.usbmodem00001',9600)

#this object manages serial communication between
#arduino and RPi

#format for serial communication
#signal strength, attention, meditation, delta, theta, low alpha, high alpha, low beta, high beta, low gamma, high gamma




#returns signal quality value
#a null object is returned when the signal quality drops
#a byte like object is returned if successful
#works as of May 4th !
def getSignalQuality(duration):


    #print("entered method")
    startTime = time.time()
    while(time.time() < startTime + duration):
        #print("entered while loop")
        read_serial = ser.readline()
       #print("read serial port ")
        #myByteList[0] = read_serial.split(b",")
       # print("made list")

    myByteList = read_serial.split(b",")
    #returns byte object for signal quality
    #print("about to finish method and return")
    return myByteList[0]

#returns attention value
#for a duration in seconds(int)
#works as of May 4th
def getAttention(duration, read_serial=None):

    startTime = time.time()
    #this is to ensure that we have a healthy signal
    # 0 is full connection, 200 is no connection to headset
    # recall that these are byte like objects as well

    while (time.time() < startTime + duration and getSignalQuality(duration)== b'0') :
        read_serial = ser.readline()

    myByteList = read_serial.split(b",")
    return myByteList[1]