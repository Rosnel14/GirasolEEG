#This is the library for screen control 
import pyautogui
import math
import time

#This is for returning info on the display
def monitorInfo(): 

    width_height = pyautogui.size()
    print(width_height)
    print(width_height[0])
    print(width_height[1])

#Moving the relative position of the cursor
def moveCursor():
    
    #move to x,y coordinate
    pyautogui.move(100,0,duration=1)
    pyautogui.move(0,100,duration=1)
    pyautogui.move(-100,0,duration=1)
    pyautogui.move(0,-100,duration=1)

def mouseClick():
    pyautogui.click(pyautogui.position())
    
def mouseScroll():
    pyautogui.scroll(10)
    
def circleDraw():
    time.sleep(5)
    (x,y) = pyautogui.size()
    (X,Y) = (int(x/2), int(y/2))
    pyautogui.click((X,Y))
    pyautogui.moveTo(X, Y+50)
    for i in range(361):
        if i%6==0:
            pyautogui.dragTo(X+50*math.sin(math.radians(i)), Y+50*math.cos(math.radians(i)))
    pyautogui.click((X-20,Y-20))
    pyautogui.click((X+20,Y-20))
    pyautogui.click((X,Y))
    
    for i in range(-90,90):
        if i%6==0: #speed
            pyautogui.dragTo(X+20*math.sin(math.radians(i)),Y+20*math.cos(math.radians(i)))
    pyautogui.dragTo(X,Y)
def main():
    #circleDraw()

    moveCursor()

if __name__ == "__main__":
    main()
