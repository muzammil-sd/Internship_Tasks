#Question 14 - Problem Name: Set .intersection() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

if __name__ == '__main__':
    n = input()
    set_n = set(map(int, input().split()))
    b = input()
    set_b = set(map(int, input().split()))
    
    print(len(set_n.intersection(set_b)))