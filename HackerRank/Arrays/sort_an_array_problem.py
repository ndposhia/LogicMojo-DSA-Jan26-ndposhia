#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sort_an_array' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def sort_an_array(n, arr):
    k = n-1
    j=0
    i=0
    
    while (j<=k):
        if arr[j]==2:
            arr[j], arr[k] = arr[k], arr[j]
            k-=1
        elif arr[j]==0:
            arr[j], arr[i] = arr[i], arr[j]
            j+=1
            i+=1
        else:
            j+=1
        
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = sort_an_array(n, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
