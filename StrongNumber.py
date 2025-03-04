"""
Strong Number - if the sum of factorial of each digit in a given number is equal to number itself
145 = 1! + 4! + 5!
"""

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)


def strongNumber(n):
    temp = n
    sum = 0
    while temp > 0:
        rem = temp % 10
        sum += factorial(rem)
        temp = temp // 10
    return sum==n

for i in range(1, 1000000):
    if strongNumber(i):
        print(f"{i} is a Strong Number")