#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'left_right' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def left_right(arr):
    l_max = arr[0]
    
    for i in range(1,len(arr)-1):
        if arr[i] > l_max:
            l_max = arr[i]
            if arr[i+1] > l_max:
                return l_max
            
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = left_right(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
