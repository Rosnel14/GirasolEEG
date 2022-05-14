# Importing the library

import serialParser
import time
import pyautogui
import ast

#threshold to say that user is concentrating
attn_Const = b'50'

#threshold for 'limb movement'
#current setting of 5000 seems controllable
gamma_const = b'4000'
#cursor constants
mouse_duration =1

mouse_x_duration = 100

mouse_y_duration = 100

#packet delay

delay = 2

#this moves the cursor in the y direction depending
#on if it passes a threshold
def mouseYmovement(duration):
    if(serialParser.getGamma(duration) >= gamma_const):
        print('move up')
        moveUp(duration)
    if (serialParser.getGamma(duration) <= gamma_const):
        print('move down')
        moveDown(duration)

#this moves the cursor in the x direction depending
#on if it passes a threshold
def mouseXmovement(duration):
    if(serialParser.getAttention(duration) > attn_Const):
        print('move right')
        moveRight(duration)
    if (serialParser.getAttention(duration) < attn_Const):
        print('move left')
        moveLeft(duration)

#this moves the cursor up
def moveUp(duration):
    initVal = serialParser.getGamma(duration)
    startTime = time.time()
    # as long as the current value is constantly decreasing
    while (time.time() < startTime + duration):
        while (serialParser.getGamma(duration) >= initVal):
            pyautogui.move(0, -mouse_y_duration, mouse_duration)

#this moves the cursor down
def moveDown(duration):
    initVal = serialParser.getGamma(duration)
    startTime = time.time()
    # as long as the current value is constantly decreasing
    while (time.time() < startTime + duration):
        while (serialParser.getGamma(duration) <= initVal):
            pyautogui.move(0, mouse_y_duration, mouse_duration)

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

#This method, while finalized on the week of May 13th is kinda buggy
#more work must be done to get accurate movement of the cursor
def standardOp(duration):
    #I'm trying to make a failsafe to leave this script in case it goes bad
    try:
        #I have no better loop condition
        while(True):
            mouseXmovement(duration)
            mouseYmovement(duration)
    except KeyboardInterrupt:
        print("You have interuptted Brain Interface Device")
        print("Restart Script")



#method that is actually run
def main():


    #main operation
    standardOp(delay)


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
    #mouseXmovement(delay)

    #yMovement
    #mouseYmovement(delay)
    #mouseYmovement(delay)
    #moveDown(delay)




    #testing heap method
    #serialParser.getSignalQualityHeap(delay)

#entry point for program
if __name__ == "__main__":
    main()
