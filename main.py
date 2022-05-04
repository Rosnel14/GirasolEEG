# Importing the library
import pygame
import serial
import pyautogui
import serialParser


#serial input from arduino
#for RPi /dev/ttyACM0 for serial path
#for MacOS /dev/cu.usbmodem00001
ser = serial.Serial('/dev/cu.usbmodem00001',9600)

#threshold to say that user is concentrating
attn_Const = 50;

#threshold to say user is meditating (eyes closed)
med_Const = 70;

#threshold to say user
theta_Constant = 6000;




def main():
    serialParser.getAttention(5)



#entry point for program
if __name__ == "__main__":
    main()
