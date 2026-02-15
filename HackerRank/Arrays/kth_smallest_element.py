#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kthSmallest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr1
#  3. INTEGER m
#  4. INTEGER_ARRAY arr2
#  5. INTEGER k
#

def kthSmallest(m, arr1, n, arr2, k):
    n1 = m
    n2 = n
    
    if n1>n2:
        return kthSmallest(n,arr2,m,arr1,k)
    i = max(0,k-n2)
    j = min(k,n1)
    
    while i<=j:
        mid1 = (i+j)//2
        mid2 = abs(k-mid1)
        print(mid1,mid2)
        l1 = -float('inf')
        l2 = -float('inf')
        r1 = float('inf')
        r2 = float('inf')
        
        if mid1<n1:
            r1 = arr1[mid1]
        if mid2<n2:
            r2 = arr2[mid2]
        if mid1-1>=0:
            l1 = arr1[mid1-1]
        if mid2-1>=0:
            l2 = arr2[mid2-1]

        
        if l1<=r2 and l2<=r1:
            return str(max(l1,l2))
        elif l1>r2:
            j = mid1 - 1
        else:
            i = mid1 + 1
            
    return str(0.0)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr1 = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    arr2 = list(map(int, input().rstrip().split()))

    k = int(input().strip())

    result = kthSmallest(n, arr1, m, arr2, k)

    fptr.write(str(result) + '\n')

    fptr.close()
