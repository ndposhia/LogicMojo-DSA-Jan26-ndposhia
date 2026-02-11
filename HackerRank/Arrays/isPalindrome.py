#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def isPalindrome(s):
    i = 0
    j = len(s)-1
    
    while i <= j:
        if s[i]!=s[j]:
            return 0
        i+=1
        j-=1
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()
