#Question 20 - Problem Name: Super Reduced String
# HackerRank Link: https://www.hackerrank.com/challenges/reduced-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def superReducedString(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    return "".join(stack) if stack else "Empty String"

if __name__ == '__main__':
    s = input().strip()
    print(superReducedString(s))