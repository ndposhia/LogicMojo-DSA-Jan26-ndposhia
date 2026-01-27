#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDistinctCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def findDistinctCount(n, arr):
    i = 0
    j = n-1
    count = 1
    while i < j:
        if abs(arr[i])<abs(arr[j]):
            if abs(arr[j])!=abs(arr[j-1]):
                count+=1
            j-=1
        elif abs(i)>abs(j):
            if abs(arr[i])!=abs(arr[i+1]):
                count+=1
            i+=1
        else:
            if abs(arr[i])!=abs(arr[i+1]) and abs(arr[j])!=abs(arr[j-1]):
                count+=1
            i+=1
            j-=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findDistinctCount(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
