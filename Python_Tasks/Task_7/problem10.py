#Question 10 - Problem Name: CamelCase
# HackerRank Link: https://www.hackerrank.com/challenges/camelcase/problem

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

def camelcase(s):
    word_count = 1
    for char in s:
        if char.isupper():
            word_count += 1
    return word_count

if __name__ == '__main__':
    s = input().strip()
    print(camelcase(s))