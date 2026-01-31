#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'singlelement' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def singlelement(n, arr):
    i = 0
    j = n-1
    while i<j:
        mid = i + (j-i)//2
        if mid%2!=0:
            if arr[mid]==arr[mid-1]:
                i = mid+1
            else:
                j = mid
        else:
            if arr[mid]==arr[mid+1]:
                i = mid+1
            else:
                j = mid
    return arr[i]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = singlelement(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
