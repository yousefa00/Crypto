import pygame
import Game
import threading
lock = threading.Lock()  # Imports code that will allow two simultaneous processes
from Game import *  # Imports all variables from Game
ans = False
while not ans:
    global level  # Creates a global variable
    Game.level = input("Please choose a difficulty (Beginner, Expert, Insane): ")  # Prompts for guess and send to Game
    if Game.level.lower() == "beginner":
        print("You are a character stuck in a maze")
        print("The only way to get out is to guess the correct coordinates but...")
        print("In order to guess the next coordinates, you must decrypt the pattern from these coordinates...")
        print("Start: (0, 0)")
        print("1: (2, 2)")
        print("2: (4, 2)")
        print("3: (6, 4)")
        print("4: (8, 4)")
        ans = True
    elif Game.level.lower() == "expert":
        print("You are a character stuck in a maze")
        print("The only way to get out is to decrypt the following words")
        print("In order to guess the next coordinates, you must decrypt the pattern from this word...")
        print("Normal Word: cat")
        ans = True
    elif Game.level.lower() == "insane":
        print("You are a character stuck in a maze")
        print("The only way to get out is to decrypt the following words")
        print("In order to guess the next coordinates, you must decrypt the pattern from this word...")
        print("Normal Word: cat")
        ans = True
background = (255, 255, 255)  # Color
colorChar = (0, 0, 0)  # Color
colorLi = (255, 255, 255)  # Color
image = pygame.image.load("maze.png")  # Loads an image

pygame.init()  # Initializes modules required for pygame
screen = pygame.display.set_mode((700, 600))  # Launches window of desired size
screen.fill(background)  # Fills a background color
done = False
circle = pygame.draw.circle(screen, colorChar, (212, 275), 8, 0)  # Draws an initial circle

gameThread = threading.Thread(None, Game.game, "Game thread", (), {})
gameThread.start()  # Starts running Game simultaneously with Main

def updatepos():
    global gameThread
    global xcoor
    global ycoor
    global lock
    tmpXC = 0
    tmpYC = 0
    lock.acquire()  # Waits for unlocked variable from Game, then acquires it
    try:
        tmpXC = Game.xcoor  # Gets data from Game every time this function is called
        tmpYC = Game.ycoor
    finally:
        lock.release()  # Releases variable back to Game
        if tmpXC > 1:  # Loop that will constantly repaint everything on the screen
            screen.fill(background)   # Redraws background
            screen.blit(image, (0, 0))  # Draws an image (maze)
            line = pygame.draw.line(screen, colorLi, (8, 257), (8, 286), 5)  # Draws a line
    circle = pygame.draw.circle(screen, colorChar, (tmpXC, tmpYC), 8, 0)  # Updates position of playing character
    circle2 = pygame.draw.circle(screen, background, (0, 0), 8, 0)  # Draws a character over initial character at (0, 0)
while not done:
    for event in pygame.event.get():  # Empties previous entries to prevent game from crashing
        if event.type == pygame.QUIT:  # Runs when window is closed
            done = True  # Stops loop
#        print(event)  # Prints a list of events in console (Use this to find coordinates)
    screen.blit(image, (0, 0))  # Draws maze
    line = pygame.draw.line(screen, colorLi, (8, 257), (8, 286), 5)  # Draws a line
    updatepos()  # Runs updatepos()
    pygame.display.flip()  # Buffers screen in order for content to get displayed correctly





