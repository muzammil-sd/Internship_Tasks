#Question 19 - Problem Name: Weighted Uniform Strings
# HackerRank Link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    weights = set()
    current_weight = 0
    prev_char = ""
    
    for char in s:
        weight = ord(char) - ord('a') + 1
        if char == prev_char:
            current_weight += weight
        else:
            current_weight = weight
            prev_char = char
        weights.add(current_weight)
        
    return ["Yes" if q in weights else "No" for q in queries]

if __name__ == '__main__':
    s = input().strip()
    queries_count = int(input().strip())
    queries = [int(input().strip()) for _ in range(queries_count)]
    
    result = weightedUniformStrings(s, queries)
    print("\n".join(result))