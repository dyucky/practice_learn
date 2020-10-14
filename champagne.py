#!/usr/bin/env python3

# champagne tower:
# 100 rows of champagne
# one dimensional, once a glass is full, half goes to left and right daughter glass
# given a number of cups poured, index of glass at row i and glass j, tell how full the glass is 


def glass_fullness(cups:float, row:int, index:int) -> float:
    tower = [[cups]]


    for height in range(row+1):
        tower.append([0.0 for _ in range(height+2)])
        for glass in range(height+1):
            if (tower[height][glass] > 1.0):
                runover = tower[height][glass] - 1.0
                tower[height][glass] = 1.0
                if (height < 99):
                    tower[height+1][glass]   += runover/2.0
                    tower[height+1][glass+1] += runover/2.0

    print(tower)
    row -=1
    index -=1
    return tower[row][index]



print( glass_fullness(30.0, 5, 1))




# 1/1 #2
# 1/2 1/2 

# 1/1 #3
# 1/1 1/1

# 1/1 #4
# 1/1 1/1
# 1/4 1/2 1/4

# 1/1 #5
# 1/1 1/1
# 1/2 1/1 1/2

# 1/1 #6
# 1/1 1/1
# 3/4 1/1 3/4
# 000 1/4 1/4 000

# 1/1 #7
# 1/1 1/1
# 1/1 1/1 1/1
# 000 1/2 1/2 000

# 1/1 #8
# 1/1 1/1
# 1/1 1/1 1/1
# 1/8 7/8 7/8 1/8

# 1/1 #9
# 1/1 1/1
# 1/1 1/1 1/1
# 1/4 1/1 1/1 1/4
# 000 1/16 1/8 1/16 000




