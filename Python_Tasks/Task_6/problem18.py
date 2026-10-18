#Question 18 - Problem Name: Set Mutations
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-mutations/problem

if __name__ == '__main__':
    len_a = int(input())
    set_a = set(map(int, input().split()))
    num_mutations = int(input())
    
    for _ in range(num_mutations):
        operation, len_other = input().split()
        other_set = set(map(int, input().split()))
        
        if operation == "update":
            set_a.update(other_set)
        elif operation == "intersection_update":
            set_a.intersection_update(other_set)
        elif operation == "difference_update":
            set_a.difference_update(other_set)
        elif operation == "symmetric_difference_update":
            set_a.symmetric_difference_update(other_set)
            
    print(sum(set_a))