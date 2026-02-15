#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'median_array' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums1
#  2. INTEGER_ARRAY nums2
#

def median_array(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    
    if n1>n2:
        median_array(nums2,nums1)
        
    n = n1 + n2 
    left = (n+1)//2
    i = 0
    j = n1
    
    while i<=j:
        mid1 = (i+j)//2
        mid2 = left-mid1
        l1 = -float('inf')
        l2 = -float('inf')
        r1 = float('inf')
        r2 = float('inf')
        
        if mid1<n1:
            r1 = nums1[mid1]
        if mid2<n2:
            r2 = nums2[mid2]
        if mid1-1>=0:
            l1 = nums1[mid1-1]
        if mid2-1>=0:
            l2 = nums2[mid2-1]
    
        
        if l1<=r2 and l2<=r1:
            if n % 2 == 1:
                return str(max(l1,l2))
            return str((max(l1,l2)+min(r1,r2))/2)
        elif l1>r2:
            j = mid1 - 1
        else:
            i = mid1 + 1
            
    return str(0.0)
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    nums1 = list(map(int, input().rstrip().split()))

    nums2 = list(map(int, input().rstrip().split()))

    result = median_array(nums1, nums2)

    fptr.write(result + '\n')

    fptr.close()
