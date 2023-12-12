#Importing modules
import pygame
from pygame.locals import *

#Initializing pygame
pygame.init()

#Global variables
HEIGHT = 600
WIDTH = 800
BOXSIZE = 50
FPS = 60/8
snake_size = 1
snakeX = WIDTH/2
snakeY = HEIGHT/2
snakeDirectionX = 0
snakeDirectionY = 0

#Rendering window
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("The Snake Game")

running = True

def drawLines():
    i = BOXSIZE
    while i < WIDTH:
        pygame.draw.line(screen, (255, 255, 255), (i, 0), (i, HEIGHT), 2)
        pygame.draw.line(screen, (255, 255, 255), (0, i), (WIDTH, i), 2)
        i = i +BOXSIZE


def rect():
    i = 0
    while i != snake_size:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(snakeX, snakeY, BOXSIZE, BOXSIZE))
        i = i+1

while running:
    screen.fill((0, 0, 0))
    drawLines()
    rect()
    
    snakeX += snakeDirectionX
    snakeY += snakeDirectionY
    
    if(snakeY == 0 or snakeY == HEIGHT - BOXSIZE):
        snakeDirectionY = 0
    if(snakeX == 0 or snakeX == WIDTH - BOXSIZE):
        snakeDirectionX = 0
    
    # for loop through the event queue   
    for event in pygame.event.get(): 
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snakeDirectionY = -BOXSIZE
                snakeDirectionX = 0
            if event.key == pygame.K_DOWN:
                snakeDirectionY = BOXSIZE
                snakeDirectionX = 0
            if event.key == pygame.K_LEFT:
                snakeDirectionX = -BOXSIZE
                snakeDirectionY = 0
            if event.key == pygame.K_RIGHT:
                snakeDirectionX = BOXSIZE
                snakeDirectionY = 0 

    pygame.display.update()
    pygame.time.Clock().tick(FPS)
