#Question 16 - Problem Name: Check Subset
# HackerRank Link: https://www.hackerrank.com/challenges/py-check-subset/problem

if __name__ == '__main__':
    test_cases = int(input())
    
    for _ in range(test_cases):
        a_count = input()
        set_a = set(map(int, input().split()))
        b_count = input()
        set_b = set(map(int, input().split()))
        
        print(set_a.issubset(set_b))