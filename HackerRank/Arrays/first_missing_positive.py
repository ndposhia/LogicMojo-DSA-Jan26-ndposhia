#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'first_missing_positive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def first_missing_positive(n, arr):
    for i in range(n):
        if arr[i]<1 or arr[i]>n:
            arr[i]=n+1
            
    for i in range(n):
        if abs(arr[i])<=n:
            index = abs(arr[i])-1
            if arr[index]>0:
                arr[index]=-arr[index]
            
    for i in range(n):
        if arr[i]>0:
            return i+1
    return n+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = first_missing_positive(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
