#Importing modules
import pygame
from pygame.locals import *

#Initializing pygame
pygame.init()

#Global variables
HEIGHT = 600
WIDTH = 800
BOXSIZE = 50
snake_size = 1
snakeX = WIDTH/2
snakeY = HEIGHT/2

#Rendering window
screen = pygame.display.set_mode((WIDTH,HEIGHT))

running = True

def drawLines():
    i = BOXSIZE
    while i < WIDTH:
        pygame.draw.line(screen, (255, 255, 255), (i, 0), (i, HEIGHT), 2)
        pygame.draw.line(screen, (255, 255, 255), (0, i), (WIDTH, i), 2)
        i = i +BOXSIZE

drawLines()

def rect():
    i = 0
    while i != snake_size:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(snakeX, snakeY, BOXSIZE*snake_size/2, BOXSIZE/2))
        i = i+1

while running:
    rect()
    snakeX = snakeX + 1/100
    # for loop through the event queue   
    for event in pygame.event.get(): 
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

    pygame.display.update()
