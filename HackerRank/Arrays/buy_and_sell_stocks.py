#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxProfit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER n
#

def maxProfit(nums, n):
#     profit = 0
#     max_profit = 0
#     min_so_far = nums[0]
    
#     for i in range(1,n):
#         profit = nums[i] - min_so_far
#         max_profit = max(profit, max_profit)
#         min_so_far = min(nums[i], min_so_far)
        
#     return max_profit

    b = nums[0]
    total = 0
    p = 0
    for i in range(1,n):
        if nums[i]-b>0:
            p = nums[i]-b
            b = nums[i]
            total+=p
        elif nums[i]<b:
            b = nums[i]
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    profit = maxProfit(price, n)

    fptr.write(str(profit) + '\n')

    fptr.close()
