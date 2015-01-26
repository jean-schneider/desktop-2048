#================================================
#=                       2048                   =
#================================================
# J.Schneider
# 10/14-01/15

# Version 0.7 - BETA

#################### MAIN PROGRAM #################
# Part of the 2048 for PC Project.
#
# Required libraries:
#   o display.py
#   o fcts.py
#   o moove.py



import pygame
from pygame.locals import *
import move
from fcts import *
from display import *

N=4 #Nb of squares (default:4)
tab = [None]*N
for i in range(N):
    tab[i]=[0]*N

GetImages()
produce_number(tab,N)
produce_number(tab,N)

true=True

show(tab,N)
while true:
    
    
    for event in pygame.event.get():
        show(tab,N)
        if event.type == QUIT:
            true = False
            pygame.quit()
        
#        Listen to keyboard events
        if event.type == KEYDOWN:
            if event.key == K_UP:
                no=moove.GoUp(tab,N)
                if no!=0:
                    produce_number(tab,N)

            elif event.key == K_LEFT:
               no=moove.GoLeft(tab,N)
               if no!=0:
                   produce_number(tab,N)

            elif event.key == K_RIGHT:
               no=moove.GoRight(tab,N)
               if no!=0:
                   produce_number(tab,N)
                        
            elif event.key == K_DOWN:
               no=moove.GoDown(tab,N)
               if no!=0:
                   produce_number(tab,N)
                  
        loose=test(tab,N)
        if loose==0:
            print("Game over")
        

    
    


    
