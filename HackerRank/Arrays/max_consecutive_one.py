#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'max_consecutive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def max_consecutive(arr):
    max_count = 0
    count = 0
    
    for i in range(n):
        if arr[i] == 1:
            count+=1
            max_count = max(count, max_count)
        else:
            count = 0
            
    return max_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = max_consecutive(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
