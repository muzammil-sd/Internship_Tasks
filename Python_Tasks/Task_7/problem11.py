#Question 11 - Problem Name: Two Strings
# HackerRank Link: https://www.hackerrank.com/challenges/two-strings/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    if set(s1).intersection(set(s2)):
        return "YES"
    return "NO"

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s1 = input().strip()
        s2 = input().strip()
        print(twoStrings(s1, s2))