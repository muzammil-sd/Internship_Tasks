#Question 10 - Problem Name: Designer Door Mat
# HackerRank Link: https://www.hackerrank.com/challenges/designer-door-mat/problem

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    for i in range(1, n, 2):
        pattern = (".|." * i).center(m, "-")
        print(pattern)
        
    print("WELCOME".center(m, "-"))
    
    for i in range(n - 2, 0, -2):
        pattern = (".|." * i).center(m, "-")
        print(pattern)