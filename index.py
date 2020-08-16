## 1-9 
import numpy as np
chart = [
    [
        5,3,0,0,7,0,0,0,0
    ],
    [
        6,0,0,1,9,5,0,0,0
    ],
    [
        0,9,8,0,0,0,0,6,0
    ],
    [
        8,0,0,0,6,0,0,0,3
    ],
    [
        4,0,0,8,0,3,0,0,1
    ],
    [
        7,0,0,0,2,0,0,0,6
    ],
    [
        0,6,0,0,0,0,2,8,0
    ],
    [
        0,0,0,4,1,9,0,0,5
    ],
    [
        0,0,0,0,8,0,0,7,9
    ],
]

def solve():
    global chart
    for y in range(9):
        for x in range(9):
            if chart[y][x] == 0:
                for n in range(1,10):
                    if canUse(n,x,y):
                        chart[y][x] = n
                        solve()
                        chart[y][x] = 0
                return
    print(np.matrix(chart))
    input("")

def canUse(number,xLine,yLine):
    global chart
    for a in range(9):
        if number == chart[yLine][a]:
            return False

    for a in range(9):
        if number == chart[a][xLine]:
            return False
    
    x0 = (xLine//3)*3
    y0 = (yLine//3)*3

    for i in range(3):
        for j in range(3):
            if number == chart[y0+i][x0+j]:
                return False
    
    return True
    
             
solve()