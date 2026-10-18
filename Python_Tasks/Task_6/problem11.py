#Question 11 - Problem Name: String Formatting
# HackerRank Link: https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        dec_val = str(i).rjust(width)
        oct_val = oct(i)[2:].rjust(width)
        hex_val = hex(i)[2:].upper().rjust(width)
        bin_val = bin(i)[2:].rjust(width)
        print(f"{dec_val} {oct_val} {hex_val} {bin_val}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)