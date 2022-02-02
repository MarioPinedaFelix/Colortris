from pickle import TRUE
import pygame
import random
from pygame import mixer
pygame.init()
color = 5

#screen size-------------------------------------------------

screen = pygame.display.set_mode((1000, 800))


#background, title, and image title--------------------------

pygame.display.set_caption("Colortris")
icon = pygame.image.load('circle.png')
pygame.display.set_icon(icon)
pygame.display.update()



#images-------------------------------------------

titleImg = pygame.image.load('colortrisdos.png')
separationImg =  pygame.image.load('idkman.png')
startImg =  pygame.image.load('sg1.png')
leaderboardImg =  pygame.image.load('lb1.png')
exitImg =  pygame.image.load('exit1.png')
arrow = pygame.image.load('arrows.png')

test_surface = pygame.Surface((800,1000))
test_surface.fill('Black')

redclone = pygame.image.load('1red.png')
blueclone = pygame.image.load('1blue.png')
greenclone = pygame.image.load('1green.png')
pinkclone = pygame.image.load('1pink.png')




#chooses which color is gonna be-----------------------------------------
number = random.randint(1, 4)

if number == 1:
    player = pygame.image.load('1red.png')

if number == 2:
    player = pygame.image.load('1blue.png')

if number == 3:
    player = pygame.image.load('1green.png')

if number == 4:
    player = pygame.image.load('1pink.png')
    
playerX = 0
playerY = -600



#--------------------------------------



#game loop------------------------------------

running = True
while running:
    
    
    screen.fill((0, 0, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False

        


    
#Movement--------------------------------------------------
    keys = pygame.key.get_pressed()
     
    
    
    if (playerX > -100) and (keys[pygame.K_LEFT]) and (playerY < 100):
           playerX -=100

    if (playerX < 200) and (keys[pygame.K_RIGHT]) and (playerY < 100):
           playerX +=100

    if (playerY < 100) and (keys[pygame.K_DOWN]):
           playerY += 6

    if playerY < 100:
              playerY += 2



#images----------------------------------------

    screen.blit(test_surface,(465,0))
    screen.blit(titleImg,(-650,-200))
    screen.blit(separationImg,(450,0))
    screen.blit(arrow,(-730,0))
    #screen.blit(startImg,(90,250))
    #screen.blit(leaderboardImg,(80,350))
    #screen.blit(exitImg,(175,450))

    screen.blit(player, (playerX, playerY))
    
    
    

#Respawns upon falling-----------------------------------------
 
    cloneX = playerX

    if color == 1:
         screen.blit(redclone, (cloneX, 100))   
    if color == 2:
         screen.blit(blueclone, (cloneX, 100))
    if color == 3:
         screen.blit(greenclone, (cloneX, 100))
    if color == 4:
         screen.blit(pinkclone, (cloneX, 100))

#red clone
    if (playerY >= 100) and (number == 1):
        print("1")
        color = 1
        number = random.randint(1, 4)
        playerX = 0
        playerY = -600

#blue clone
    if (playerY >= 100) and (number == 2):
        print("2")
        color = 2 
        number = random.randint(1, 4)
        playerX = 0
        playerY = -600

#green clone
    if (playerY >= 100) and (number == 3):
        print("3")
        color = 3
        number = random.randint(1, 4)
        playerX = 0
        playerY = -600

#pink clone
    if (playerY >= 100) and (number == 4):
        print("4")
        color = 4
        number = random.randint(1, 4)
        playerX = 0
        playerY = -600


    
   
    
        

    
    pygame.display.update()