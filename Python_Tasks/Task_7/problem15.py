#Question 15 - Problem Name: Game of Thrones - I
# HackerRank Link: https://www.hackerrank.com/challenges/game-of-thrones/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

import collections

def gameOfThrones(s):
    counts = collections.Counter(s)
    odd_counts = sum(1 for v in counts.values() if v % 2 != 0)
    
    if odd_counts <= 1:
        return "YES"
    return "NO"

if __name__ == '__main__':
    s = input().strip()
    print(gameOfThrones(s))