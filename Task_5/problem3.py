#Question 3 -
#Problem Name - Mutations
#HackerRank Link - https://www.hackerrank.com/challenges/python-mutations/problem

#Read a given string, change the character at a given index and then print the modified string.

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    inp, ch = input().split()
    s_new = mutate_string(s, int(inp), ch)
    print(s_new)
