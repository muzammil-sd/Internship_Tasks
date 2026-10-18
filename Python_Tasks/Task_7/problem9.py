#Question 9 - Problem Name: Beautiful Binary String
# HackerRank Link: https://www.hackerrank.com/challenges/beautiful-binary-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    return b.count("010")

if __name__ == '__main__':
    n = int(input().strip())
    b = input().strip()
    print(beautifulBinaryString(b))