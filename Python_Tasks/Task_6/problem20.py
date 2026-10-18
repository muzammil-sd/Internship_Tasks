#Question 20 - Problem Name: Validating the Phone Number
# HackerRank Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

if __name__ == '__main__':
    n = int(input())
    
    pattern = r"^[789]\d{9}$"
    
    for _ in range(n):
        phone_num = input().strip()
        if re.match(pattern, phone_num):
            print("YES")
        else:
            print("NO")