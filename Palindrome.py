# Find 3 largest 9 digit palindrome prime numbers

from math import pow


def printPalindrome(n):
    if n == 1:
        print("Smallest Palindrome : 0")
        print("Largest Palindrome: 1")
    else:
        print("Smallest Palindrome :", int(pow(10, n - 1)) + 1)
        print("Largest Palindrome :", int(pow(10, n)) - 1)


if __name__ == '__main__':
    n = int(input("Enter the value: "))
    printPalindrome(n)
