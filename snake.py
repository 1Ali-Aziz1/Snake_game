#Importing modules
import pygame
import random
from pygame.locals import *

#Initializing pygame
# pygame.init()

#Global variables
screenHeight = 600
screenWidth = 800
BOXSIZE = 50
FPS = 60/10
snake_size = 0
snakeX = screenWidth/2
snakeY = screenHeight/2
snakeList = []
snakeDirectionX = 0
snakeDirectionY = 0
foodX = []
foodY = 0
line = False
temp = 0

# for i in range(1, 17):
#     foodX.append(i*BOXSIZE)

# foodX.append(50)
# foodX.append(100)

print(foodX)

 

#Rendering window
pygame.display.set_caption("The World's Best Snake Game")

running = True

def drawLines():
    if line:
        i = BOXSIZE
        while i < screenWidth:
            pygame.draw.line(screen, (255, 255, 255), (i, 0), (i, screenHeight), 2)
            pygame.draw.line(screen, (255, 255, 255), (0, i), (screenWidth, i), 2)
            i = i +BOXSIZE


def rect():
    # i = 0
    # while i != snake_size:
    #     pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(snakeX + i*BOXSIZE, snakeY, BOXSIZE, BOXSIZE))
    #     i = i+1
    i = 0
    # i = 1
    for x,y in snakeList:
        j = i
        if i >=250:
          i=0
        pygame.draw.rect(screen, (i, 255, i), pygame.Rect(x, y, BOXSIZE, BOXSIZE))
        i += 5
        
def changeFoodLocation():
    foodX = random.randint(BOXSIZE, screenWidth - BOXSIZE)/25
    foodY = random.randint(BOXSIZE, screenHeight-BOXSIZE)/25
    return [foodX*25, foodY*25]
        
def plotFood():
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(foodX, foodY, BOXSIZE, BOXSIZE))
    
foodLocation = changeFoodLocation()
foodX = foodLocation[0]
foodY = foodLocation[1]
     


while running:
    screen = pygame.display.set_mode((screenWidth,screenHeight))
    # pygame.display.flip()
    screen.fill((0, 0, 0))
    drawLines()
    plotFood()
    rect()
    
    snakeX += snakeDirectionX
    snakeY += snakeDirectionY
    

    for x in snakeList:
        if(x == 0):
            snakeDirectionX = 0
    for y in snakeList:
        if(y == 0):
            snakeDirectionY = 0
    if(snakeX < 0):
        snakeX = 0
        
    # if(snakeX == screenWidth - BOXSIZE or snakeX > screenWidth - BOXSIZE):
    #     snakeX = screenWidth - BOXSIZE
    # if(snakeY < 0):
    #     snakeY = 0
    # if(snakeY == screenHeight - BOXSIZE or snakeY > screenWidth - BOXSIZE):
    #     snakeY = screenHeight - BOXSIZE
    
    # if(snakeY == 0 or snakeY == screenHeight - BOXSIZE):
    #     snakeDirectionY = 0
    # if(snakeX == 0 or snakeX == screenWidth - BOXSIZE):
    #     snakeDirectionX = 0
        
    head = []
    head.append(snakeX)
    head.append(snakeY)
    snakeList.append(head)
    
    if(snake_size == 0):
        snake_size = snake_size + 1
        snakeX = screenWidth/2
        snakeY = screenHeight/2
    if(abs(snakeX - foodX)<50):
        if(abs(snakeY - foodY)<50):
            snake_size += 1
            foodlocation = changeFoodLocation()
            foodX = foodlocation[0]
            foodY = foodlocation[1]
    if len(snakeList)>snake_size:
        del snakeList[0]
    #Collision of snake to walls
    if(snakeList[0][0]==0-BOXSIZE)or(snakeList[0][0]==screenWidth)or(snakeList[0][1]==screenHeight)or(snakeList[0][1]==0-BOXSIZE):
        num = 1
        for x in range(len(snakeList)):
            snake_size = snake_size - 1
            del snakeList[snake_size-1]
            snakeDirectionX = 0
            snakeDirectionY = 0
            print("lalalala")
    # for x,y in snakeList:
    #     if(abs(snakeList[0][1] - x)<50):
    #         if abs(snakeList[0][0] - y)<50:
    #             temp = temp + 1
    #             print("Ohhh lala", temp)
    
    # for loop through the event queue   
    for event in pygame.event.get(): 
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if(snakeDirectionY != BOXSIZE):
                    snakeDirectionY = -BOXSIZE
                    snakeDirectionX = 0
            if event.key == pygame.K_DOWN:
                if(snakeDirectionY != -BOXSIZE):
                    snakeDirectionY = BOXSIZE
                    snakeDirectionX = 0
            if event.key == pygame.K_LEFT:
                if(snakeDirectionX != BOXSIZE):
                    snakeDirectionX = -BOXSIZE
                    snakeDirectionY = 0
            if event.key == pygame.K_RIGHT:
                if(snakeDirectionX != -BOXSIZE):
                    snakeDirectionX = BOXSIZE
                    snakeDirectionY = 0 
            if event.key == pygame.K_w:
                snake_size += 1
            if event.key == pygame.K_s:
                snake_size -= 1
            if event.key == pygame.K_SPACE:
                snakeDirectionX = 0
                snakeDirectionY = 0
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_c:
                if line == False:
                    line = True
                elif line:
                    line = False
            if event.key == pygame.K_m:
                screenHeight = screenHeight+200
                screenWidth = screenWidth+200
            if event.key == pygame.K_n:
                if screenHeight!= 600 and screenWidth != 800:
                    screenHeight = screenHeight-200
                    screenWidth = screenWidth-200
                

    pygame.display.update()
    pygame.time.Clock().tick(FPS)
