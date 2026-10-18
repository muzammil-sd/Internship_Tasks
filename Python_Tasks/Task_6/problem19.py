#Question 19 - Problem Name: Company Logo
# HackerRank Link: https://www.hackerrank.com/challenges/most-commons/problem

import collections

if __name__ == '__main__':
    s = input().strip()
    
    sorted_s = sorted(s)
    
    counts = collections.Counter(sorted_s)
    
    top_three = counts.most_common(3)
    
    for char, freq in top_three:
        print(f"{char} {freq}")