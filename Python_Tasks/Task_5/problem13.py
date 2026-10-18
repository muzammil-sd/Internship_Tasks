#Question13-
#Problem Name - Nested Lists
#HackerRank Link - https://www.hackerrank.com/challenges/nested-list/problem

# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    unique_scores = sorted(set(score for name, score in students))
    second_lowest = unique_scores[1]
    
    result_names = sorted([name for name, score in students if score == second_lowest])
    
    for name in result_names:
        print(name)
