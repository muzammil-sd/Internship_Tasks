#Question 4 - Problem Name: Funny String
# HackerRank Link: https://www.hackerrank.com/challenges/funny-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    rev = s[::-1]
    for i in range(1, len(s)):
        diff_s = abs(ord(s[i]) - ord(s[i-1]))
        diff_r = abs(ord(rev[i]) - ord(rev[i-1]))
        if diff_s != diff_r:
            return "Not Funny"
    return "Funny"

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        print(funnyString(s))