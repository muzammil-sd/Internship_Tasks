#Question 18 - Problem Name: String Construction
# HackerRank Link: https://www.hackerrank.com/challenges/string-construction/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):
    return len(set(s))

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        print(stringConstruction(s))