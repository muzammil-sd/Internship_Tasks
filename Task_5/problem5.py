#Question 5 -
#Problem Name - String Validators
#HackerRank Link - https://www.hackerrank.com/challenges/string-validators/problem

#Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

if __name__ == '__main__':
    s = input()
    
    print(any(c.isalnum() for c in s))
    
    print(any(c.isalpha() for c in s))
    
    print(any(c.isdigit() for c in s))
    
    print(any(c.islower() for c in s))
    
    print(any(c.isupper() for c in s))
