#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.

# The function accepts INTEGER_ARRAY arr as parameter.
pos = 0
neg = 0
zero = 0

def plusMinus(arr):
    global pos, neg, zero
    # Write your code here
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
        elif i==0:
            zero+=1
            
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
    print(round(float(pos/len(arr)),6))
    print(round(float(neg/len(arr)),6))
    print(round(float(zero/len(arr)),6))

