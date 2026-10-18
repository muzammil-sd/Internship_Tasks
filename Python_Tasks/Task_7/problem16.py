#Question 16 - Problem Name: Caesar Cipher
# HackerRank Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    result = []
    for char in s:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + k) % 26 + base)
            result.append(shifted)
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    print(caesarCipher(s, k))