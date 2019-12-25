# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:47:51 2019

@author: elsav
"""
import numpy as np

board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
]

board = np.array(board)
z = np.argwhere(board==0)

def d():

    z = np.argwhere(board==0)
    
    for i in z:
        
        #board[i[0],i[1]] = 1, use this code to locate the zero's apart from the other non zeros at the start
        
#this is past code, not deleting because it might be helpful later to reference
#         if checkrow(i[0]) == False and checkcol(i[1]) == False:
#             board[i[0],i[1]] = checkrow(i[0])
#             break
#         else:
#             board[i[0],i[1]] = max(checkrow(i[0]),checkcol(i[1]))
#             break

        
         if checkindex(i[0],i[1]) != 10:
             board[i[0],i[1]] = checkindex(i[0],i[1])
             print(z[i[0]])
         else:
             print('We done messed up')
             print(z[i])
         break

    return board

def checkindex(r,c):
    
    a = [1,2,3,4,5,6,7,8,9,10]
    a = np.array(a)
    
    for j in list(a):
        if np.isin(j,board[int(r)]) == False and np.isin(j,board[:,int(c)]) == False:
            return j
                
    
    
    
    
    
    
    