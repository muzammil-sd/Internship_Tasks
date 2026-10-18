#Question 2 - Problem Name: The Captain's Room
# HackerRank Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem

if __name__ == '__main__':
    k = int(input())
    rooms = list(map(int, input().split()))
    
    unique_rooms = set(rooms)
    sum_unique = sum(unique_rooms)
    sum_actual = sum(rooms)
    
    captain_room = (sum_unique * k - sum_actual) // (k - 1)
    print(captain_room)