#Question 3 - Problem Name: Mars Exploration
# HackerRank Link: https://www.hackerrank.com/challenges/mars-exploration/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    mismatches = 0
    pattern = "SOS"
    for i in range(len(s)):
        if s[i] != pattern[i % 3]:
            mismatches += 1
    return mismatches

if __name__ == '__main__':
    s = input().strip()
    print(marsExploration(s))