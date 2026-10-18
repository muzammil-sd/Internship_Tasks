#Question 20 -
#Problem Name - Piling Up!
#HackerRank Link - https://www.hackerrank.com/challenges/piling-up/problem

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        blocks = list(map(int, input().split()))
        
        left = 0
        right = n - 1
        current_top = float('inf')
        possible = True
        
        while left <= right:
            if blocks[left] >= blocks[right]:
                chosen = blocks[left]
                left += 1
            else:
                chosen = blocks[right]
                right -= 1
                
            if chosen <= current_top:
                current_top = chosen
            else:
                possible = False
                break
                
        print("Yes" if possible else "No")
