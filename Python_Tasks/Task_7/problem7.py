#Question 7 - Problem Name: Alphabet Rangoli
# HackerRank Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    lines = []
    
    for i in range(size):
        s = "-".join(alpha[size-1:i:-1] + alpha[i:size])
        lines.append(s.center(4 * size - 3, "-"))
        
    rangoli_pattern = "\n".join(lines[::-1] + lines[1:])
    print(rangoli_pattern)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)