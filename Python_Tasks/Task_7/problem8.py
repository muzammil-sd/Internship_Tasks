#Question 8 - Problem Name: Gemstones
# HackerRank Link: https://www.hackerrank.com/challenges/gem-stones/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    result_set = set(arr[0])
    for rock in arr[1:]:
        result_set.intersection_update(set(rock))
    return len(result_set)

if __name__ == '__main__':
    n = int(input().strip())
    arr = [input().strip() for _ in range(n)]
    print(gemstones(arr))