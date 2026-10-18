#Question 7 -
#Problem Name - Symmetric Difference
#HackerRank Link - https://www.hackerrank.com/challenges/symmetric-difference/problem

#Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N


if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))
    
    n = int(input())
    b = set(map(int, input().split()))
    
    diff = sorted(a.symmetric_difference(b))
    
    for val in diff:
        print(val)
