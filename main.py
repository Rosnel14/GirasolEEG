# Importing the library

import serialParser
import time
import pyautogui
import ast

#threshold to say that user is concentrating
attn_Const = b'50'

#cursor constants
mouse_duration =1

mouse_x_duration = 100

mouse_y_duration = 100

#packet delay

delay = 5


def mouseXmovement(duration):
    if(serialParser.getAttention(duration) > attn_Const):
        moveRight(duration)
    elif (serialParser.getAttention(duration) < attn_Const):
        moveLeft(duration)


#this will move the cursor to the left
#works as of May 6th
def moveLeft(duration):
    initVal = serialParser.getAttention(duration)
    startTime = time.time()
    #as long as the current value is constantly decreasing
    while(time.time() < startTime + duration ):
        while(serialParser.getAttention(duration) <= initVal):
            pyautogui.move(-mouse_x_duration,0,mouse_duration)

#this will move the cursor to the right
#works as of may 6th
def moveRight(duration):
    initVal = serialParser.getAttention(duration)
    startTime = time.time()
    #as long as the current value is constantly increasing
    while(time.time() < startTime + duration):
        while (serialParser.getAttention(duration) >= initVal):
            pyautogui.move(mouse_x_duration,0,mouse_duration)


def main():

    #testing each method

    #works - gets signal quality
    #print(serialParser.getSignalQuality(delay))

    # works - gets attention values
    #print(serialParser.getAttention(delay))

    #moving right
    #moveRight(delay)

    #moving left
    #moveLeft(delay)

    #xmovement
    mouseXmovement(delay)

#entry point for program
if __name__ == "__main__":
    main()
