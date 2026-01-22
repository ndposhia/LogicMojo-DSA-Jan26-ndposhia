#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rain_water' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY hei as parameter.
#

def rain_water(hei):
    i = 0
    j = len(hei)-1
    l_max = hei[i]
    r_max = hei[j]
    total = 0
    
    while(i < j):
        if hei[i] < hei[j]:
            i += 1
            if hei[i] < l_max:
                total += l_max-hei[i]
            else:
                l_max = hei[i]
        else:
            j -= 1
            if hei[j] < r_max:
                total += r_max-hei[j]
            else:
                r_max = hei[j]
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    hei = list(map(int, input().rstrip().split()))

    result = rain_water(hei)

    fptr.write(str(result) + '\n')

    fptr.close()
