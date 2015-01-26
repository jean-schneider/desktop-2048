#================================================
#=                       2048                   =
#================================================
# J.Schneider
# 10/14-01/15
#
#################### MOVE MODULE #################
# Part of the 2048 for PC Project. 

def GoUp(tab,N):
    no=0
    l=0
    # Double loop to handle the whole tab
    while  l<N:
            h=0
            while h<N:
                k=h
                if tab[k][l]!=0:
                    temp=tab[k][l]
                    while k>0:
                    
                        if tab[k-1][l]==0:
                            tab[k-1][l] = tab[k][l]
                            tab[k][l]=0
                            no=1

                        elif tab[k-1][l]==temp and tab[k][l]==tab[k-1][l]:

                            tab[k-1][l]+=1
                            tab[k][l]=0
                            no=1
                        
                        k-=1

                h+=1
            l+=1
    return no

def GoLeft(tab,N):
    no=0
    h=0
    # Double loop to handle the whole tab
    while h <N:
            l=0
            while l<N:
                k=l
                if tab[h][k]!=0:
                    temp=tab[h][k]
                    while k>0:
                    
                        if tab[h][k-1]==0:
                            tab[h][k-1] = tab[h][k]
                            tab[h][k]=0
                            no=1

                        elif tab[h][k-1]==temp and tab[h][k]==tab[h][k-1]:
                            tab[h][k-1]+=1
                            tab[h][k]=0
                            no=1
                        
                        k-=1
                l+=1
            h+=1
    return no

def GoRight(tab,N):
    no=0
    h=0
    # Double loop to handle the whole tab
    while h<N:
            l=N-2
            while l>=0:
                k=l
                if tab[h][k]!=0:
                    temp=tab[h][k]
                    while k>=0 and k<N-1:
                        
                        # Move numbers
                        if tab[h][k+1]==0:
                            tab[h][k+1] = tab[h][k]
                            tab[h][k]=0
                            no=1
                        
                        # Merging numbers
                        elif tab[h][k+1]==temp and tab[h][k]==tab[h][k+1]:
                            tab[h][k+1]+=1
                            tab[h][k]=0
                            no=1
                       
                        k+=1
                l-=1
            h+=1

    return no

def GoDown(tab,N):
    no=0
    l=0
    # Double loop to handle the whole tab
    while l<N:
            h=N-2
            while h>=0:
                k=h
                if tab[k][l]!=0:
                    temp=tab[k][l]
        
                    while k>=0 and k<N-1:
                    
                        if tab[k+1][l]==0:
                            tab[k+1][l] = tab[k][l]
                            tab[k][l]=0
                            no=1

                        elif tab[k+1][l]==temp and tab[k][l]==tab[k+1][l]:
                            tab[k+1][l]+=1
                            tab[k][l]=0
                            no=1
                       
                        k+=1
                h-=1
            l+=1

    return no
