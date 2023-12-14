#Importing modules
import pygame
import random
from pygame.locals import *

#Initializing pygame
pygame.init()

#Global variables
HEIGHT = 600
WIDTH = 800
BOXSIZE = 50
FPS = 60
snake_size = 1
snakeX = WIDTH/2
snakeY = HEIGHT/2
snakeList = []
snakeDirectionX = 0
snakeDirectionY = 0
foodX = 0
foodY = 0

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
    # i = 0
    # while i != snake_size:
    #     pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(snakeX + i*BOXSIZE, snakeY, BOXSIZE, BOXSIZE))
    #     i = i+1
    for x,y in snakeList:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x, y, BOXSIZE, BOXSIZE))
        
def changeFoodLocation():
    x = random.randint(BOXSIZE, WIDTH - BOXSIZE)
    y = random.randint(BOXSIZE, HEIGHT-BOXSIZE)
    return [x, y]
        
def plotFood():
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(foodX, foodY, BOXSIZE, BOXSIZE))
    
foodLocation = changeFoodLocation()
foodX = foodLocation[0]
foodY = foodLocation[1]
     

while running:
    screen.fill((0, 0, 0))
    # drawLines()
    plotFood()
    rect()
    
    snakeX += snakeDirectionX
    snakeY += snakeDirectionY
    

    if(snakeX == 0):
        snakeDirectionX = 0
    if(snakeY == 0):
        snakeDirectionY = 0
    if(snakeX < 0):
        snakeX = 0
        
    if(snakeX == WIDTH - BOXSIZE or snakeX > WIDTH - BOXSIZE):
        snakeX = WIDTH - BOXSIZE
    if(snakeY < 0):
        snakeY = 0
    if(snakeY == HEIGHT - BOXSIZE or snakeY > WIDTH - BOXSIZE):
        snakeY = HEIGHT - BOXSIZE
    
    if(snakeY == 0 or snakeY == HEIGHT - BOXSIZE):
        snakeDirectionY = 0
    if(snakeX == 0 or snakeX == WIDTH - BOXSIZE):
        snakeDirectionX = 0
        
    head = []
    head.append(snakeX)
    head.append(snakeY)
    snakeList.append(head)
    
    
    if(snakeX - foodX == 0):
        if(snakeY - foodY == 0):
            snake_size += 1
            foodlocation = changeFoodLocation()
            foodX = foodlocation[0]
            foodY = foodlocation[1]
    
    if len(snakeList)>snake_size:
        del snakeList[0]
    
    # for loop through the event queue   
    for event in pygame.event.get(): 
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snakeDirectionY = -BOXSIZE/BOXSIZE
                snakeDirectionX = 0
            if event.key == pygame.K_DOWN:
                snakeDirectionY = BOXSIZE/BOXSIZE
                snakeDirectionX = 0
            if event.key == pygame.K_LEFT:
                snakeDirectionX = -BOXSIZE/BOXSIZE
                snakeDirectionY = 0
            if event.key == pygame.K_RIGHT:
                snakeDirectionX = BOXSIZE/BOXSIZE
                snakeDirectionY = 0 
            if event.key == pygame.K_w:
                snake_size += 1
            if event.key == pygame.K_SPACE:
                snakeDirectionX = 0
                snakeDirectionY = 0
            if event.key == pygame.K_s:
                print("snake position:", snakeX, snakeY)
                print("food position:", foodX, foodY)
                print("Difference of X",snakeX - foodX)
                print("Difference of Y",snakeY - foodY)
                print("_____________________________________________________________________")
                

    pygame.display.update()
    pygame.time.Clock().tick(FPS)
