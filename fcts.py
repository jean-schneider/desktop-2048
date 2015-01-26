#================================================
#=                       2048                   =
#================================================
# J.Schneider
# 10/14-01/15
#
#################### FUNCTIONS MODULE #################
# Part of the 2048 for PC Project. 

from random import randint

def test(tab,N):
    game=1
    loose=0
    loop=0
    while loop < (N-1):
        if tab[loop][0]==0:
            loose=0
            break
        elif tab[loop+1][0]==tab[loop][0] or tab[loop-1][0]==tab[loop][0]:
            loose=0
        elif tab[loop][1]==tab[loop][0]:
            loose=0

        else:
            loose+=1
        loop+=1


    for loop in range (N-1):
        if tab[loop][N-1]==0:
            loose=0
            break
        elif tab[loop+1][N-1]==tab[loop][N-1] or tab[loop-1][N-1]==tab[loop][N-1]:
            loose=0
        elif tab[loop][N-2]==tab[loop][N-1]:
            loose+=0

        else:
            loose+=1

    for loop in range (N-1):
        if tab[0][loop]==0:
            loose=0
            break
        elif tab[0][loop+1]==tab[0][loop] or tab[0][loop-1]==tab[0][loop]:
            loose=0
        elif tab[1][loop]==tab[0][loop]:
            loose=0

        else:
            loose+=1

    for loop in range (N-1):
        if tab[N-1][loop]==0:
            loose=0
            break
        elif tab[N-1][loop+1]==tab[N-1][loop] or tab[N-1][loop-1]==tab[N-1][loop]:
            loose=0
        elif tab[N-2][loop]==tab[N-1][loop]:
            loose=0

        else:
            loose+=1

    for i in range (N-2):
        for j in range (N-2):
            if tab[i][j]==0:
                loose=0
                break
            if tab[i][j]==tab[i+1][j] or tab[i][j]==tab[i][j+1] or tab[i][j]==tab[i-1][j] or tab[i][j]==tab[i][j-1]:
                loose=0
            else:
                loose=1

    if loose>=15:
        game=0

    return game

def produce_number(tab,N):
    values=[1,1,1,1,1,1,1,1,1,2]
    x,y = randint(0,N-1), randint(0,N-1)
    l=0
    full=0
    while l <N-1:
        h=0
        l+=1
        while h<N-1:
            if tab[h][l]!=0:
                full+=1
            else:
                full=0
            h+=1

            
    while tab[x][y]!=0 and full!=N*N:
        x,y = randint(0,N-1), randint(0,N-1)
        
    if tab[x][y]==0:
        tab[x][y]=values[randint(0,9)]
    
    
    




