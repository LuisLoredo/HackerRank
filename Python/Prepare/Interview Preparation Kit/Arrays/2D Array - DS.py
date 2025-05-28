#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
   
    maxHourglass = -float('inf')
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            topRow = arr[i-1]
            topRowSum = sum(topRow[j-1:j+2])

            
            middleRow = arr[i]
            middleRowSum = middleRow[j]
            
            bottomRow = arr[i+1]
            bottomRowSum = sum(bottomRow[j-1:j+2])


            sumHourglass = topRowSum + middleRowSum + bottomRowSum
            
            maxHourglass = max(sumHourglass, maxHourglass)
                
    return maxHourglass
             
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
