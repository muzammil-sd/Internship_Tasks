#Question 17 - Problem Name: Separate the Numbers
# HackerRank Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem

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

def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first_num_str = s[:i]
        val = int(first_num_str)
        
        temp_str = first_num_str
        current_val = val
        while len(temp_str) < len(s):
            current_val += 1
            temp_str += str(current_val)
            
        if temp_str == s:
            print(f"YES {first_num_str}")
            return
            
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        separateNumbers(s)