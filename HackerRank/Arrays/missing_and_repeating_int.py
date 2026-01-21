#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'find_missing' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def find_missing(arr):
    ans = []
    for i in range(n):
        if arr[i]>n:
            arr[i]=n+1
            
    for i in range(n):
        if abs(arr[i])<=n:
            index = abs(arr[i])-1
            if arr[index]>0:
                arr[index]=-arr[index]
            else:
                ans.append(index+1)
            
    for i in range(n):
        if arr[i]>0:
            ans.append(i+1)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = find_missing(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
