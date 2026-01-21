#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'majorityElement' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def majorityElement(n, arr):
    ansIndex = 0
    count = 1
    for i in range(1,n):
        if arr[i] == arr[ansIndex]:
            count+=1
        else:
            count-=1
        
        if count == 0:
            count=1
            ansIndex=i
    count = 0
    for i in range(0,n):
        if arr[i] == arr[ansIndex]:
            count+=1
    if count > n/2:
        return arr[ansIndex]
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = majorityElement(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
