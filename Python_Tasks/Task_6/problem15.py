#Question 15 - Problem Name: Set .difference() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

if __name__ == '__main__':
    n = input()
    set_n = set(map(int, input().split()))
    b = input()
    set_b = set(map(int, input().split()))
    
    print(len(set_n.difference(set_b)))