#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'remove_dupli' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def remove_dupli(arr):
    if len(arr)<2:
        return len(arr)
    i = 0
    j = 1
    while j < len(arr):
        if arr[j]==arr[j-1]:
            j+=1
        else:
            i+=1
            arr[i] = arr[j]
            j+=1
    return i+1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = remove_dupli(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
