#Question 13 - Problem Name: Sherlock and the Valid String
# HackerRank Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

import collections

def isValid(s):
    counts = collections.Counter(s)
    freqs = collections.Counter(counts.values())
    
    if len(freqs) == 1:
        return "YES"
        
    if len(freqs) == 2:
        f1, f2 = list(freqs.keys())
        if (f1 == 1 and freqs[f1] == 1) or (f2 == 1 and freqs[f2] == 1):
            return "YES"

        if (abs(f1 - f2) == 1) and ((f1 > f2 and freqs[f1] == 1) or (f2 > f1 and freqs[f2] == 1)):
            return "YES"
            
    return "NO"

if __name__ == '__main__':
    s = input().strip()
    print(isValid(s))