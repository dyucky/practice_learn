#!/bin/python3

import math
import os
import random
import re
import sys



def test1(serialCode):
    if ((9 < len(serialCode)) and (len(serialCode) < 13)):
        return True
    else:
        return False

def test2(serialCode):
    print(serialCode)
    return True   

def test3(serialCode):
    print(serialCode)
    return True

def test4(serialCode):
    print(serialCode)
    return True

def test5(serialCode):
    print(serialCode)
    return True

def countCounterfeit(serialNumber):
    goodMoney = 0
    for code in serialNumber:
        if(test1(code) and test2(code[0:2]) and test3(code[3:7]) and test5(code[-1])):
            goodMoney += test5(code[-5:-1])
    return goodMoney
            


    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    serialNumber_count = int(input().strip())

    serialNumber = []

    for _ in range(serialNumber_count):
        serialNumber_item = input()
        serialNumber.append(serialNumber_item)

    result = countCounterfeit(serialNumber)

    fptr.write(str(result) + '\n')

    fptr.close()
