#Question 14 - Problem Name: Anagram
# HackerRank Link: https://www.hackerrank.com/challenges/anagram/problem

import collections

def anagram(s):
    if len(s) % 2 != 0:
        return -1
        
    mid = len(s) // 2
    s1, s2 = s[:mid], s[mid:]
    
    c1 = collections.Counter(s1)
    c2 = collections.Counter(s2)
    
    return sum((c1 - c2).values())

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        print(anagram(s))