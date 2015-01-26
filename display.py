#================================================
#=                       2048                   =
#================================================
# J.Schneider
# 10/14-01/15
# V0.7
#################### DISPLAY MODULE #################
# Part of the 2048 for PC Project. 

import pygame
from pygame.locals import *

def GetImages():
    global image
    image=[None]*13
    image[0]=pygame.image.load("images/empty.png")
    loop=1
    while loop<13:
        name=str(loop)
        file="images/"+name+".png"
        image[loop]=pygame.image.load(file)
        loop+=1

        
def show(tab,N):
    global image
    pygame.init()
    size = width, height = N*103, N*103
    bg=(240,240,210)

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("2048")
    
    screen.fill(bg)
    
    i,j=0,0
    x,y=0,0
    while i<N:
        while j<N:
            screen.blit(image[tab[i][j]],(x,y))
            x+=103
            j+=1
        
        x,j=0,0
        y+=103
        i+=1

    pygame.display.flip()



