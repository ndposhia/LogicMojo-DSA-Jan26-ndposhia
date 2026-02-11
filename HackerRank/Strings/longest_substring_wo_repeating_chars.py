#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestSubstringWithoutRepeatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def longestSubstringWithoutRepeatingCharacters(s):
    i = 0
    j = 0
    n = len(s)
    max_len = 0
    char_set = set()
    count = 0
    
    while j<n:
        if s[j] not in char_set:
            char_set.add(s[j])
            j+=1
            count+=1
        else:
            while i < j and s[j] in char_set:
                char_set.remove(s[i])
                i+=1
                count -=1
                
        max_len = max(count, max_len)
    return max_len
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = longestSubstringWithoutRepeatingCharacters(s)

    fptr.write(str(result) + '\n')

    fptr.close()
