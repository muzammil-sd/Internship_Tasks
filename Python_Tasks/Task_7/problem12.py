#Question 12 - Problem Name: Making Anagrams
# HackerRank Link: https://www.hackerrank.com/challenges/making-anagrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

import collections

def makingAnagrams(s1, s2):
    c1 = collections.Counter(s1)
    c2 = collections.Counter(s2)
    
    diff1 = c1 - c2
    diff2 = c2 - c1
    return sum(diff1.values()) + sum(diff2.values())

if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()
    print(makingAnagrams(s1, s2))