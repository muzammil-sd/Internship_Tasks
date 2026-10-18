#Question 1 - Problem Name: Set .symmetric_difference() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

if __name__ == '__main__':
    n = input()
    set_n = set(map(int, input().split()))
    b = input()
    set_b = set(map(int, input().split()))
    
    print(len(set_n.symmetric_difference(set_b)))