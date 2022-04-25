# Importing the library
import pygame
import serial

#instance variables (global)
ser = serial.Serial('/dev/ttyACM0',9600) #serial input from arduino



def serialParser():

      change = False # track whether concentrating or not

      while(change == False): #



def main():
    screen_loop()

def screen_loop():
    # Initializing Pygame
    pygame.init()

    # Initializing surface
    surface = pygame.display.set_mode((400, 300))

    # Initialing RGB Color
    color = (255, 0, 0)

    while(True):

        # Changing surface color
        surface.fill(color)
        pygame.display.flip()

        # Initialing RGB Color
        color1 = (0, 0, 255)

        # Changing surface color
        surface.fill(color1)
        pygame.display.flip()





if __name__ == "__main__": #entry point for program
    main()