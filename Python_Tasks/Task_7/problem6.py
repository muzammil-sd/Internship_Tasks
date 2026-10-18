#Question 6 - Problem Name: Pangrams
# HackerRank Link: https://www.hackerrank.com/challenges/pangrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    chars = set(s.lower().replace(" ", ""))
    if len(chars) == 26:
        return "pangram"
    return "not pangram"

if __name__ == '__main__':
    s = input()
    print(pangrams(s))