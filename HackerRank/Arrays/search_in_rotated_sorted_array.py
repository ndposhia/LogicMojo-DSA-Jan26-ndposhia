#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'search_element' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER target
#

def search_element(arr, target):
    i = 0
    n = len(arr)
    j = n-1

    while i <= j:
        mid = i+(j-i)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>arr[j]:
            if target >= arr[i] and target < arr[mid]:
                j = mid - 1
            else:
                i = mid + 1
        else:
            if target > arr[mid] and target <= arr[j]:
                i = mid + 1
            else:
                j = mid - 1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    target = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = search_element(arr, target)

    fptr.write(str(result) + '\n')

    fptr.close()
