#Question19-
#Problem Name - Collections.Counter()
#HackerRank Link - https://www.hackerrank.com/challenges/collections-counter/problem

#Raghu is a shoe shop owner. His shop has X number of shoes.
#He has a list containing the size of each shoe he has in his shop.
#There are N number of customers who are willing to pay Xi amount of money only if they get the shoe of their desired size.
#Your task is to compute how much money Raghu earned.

from collections import Counter

if __name__ == '__main__':
    x = int(input())
    
    shoe_sizes = Counter(map(int, input().split()))
    
    n = int(input())
    
    total_earned = 0
    
    for _ in range(n):
        size, price = map(int, input().split())
        
        if shoe_sizes[size] > 0:
            total_earned += price
            
    print(total_earned)