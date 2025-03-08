"""
primes in a given range
"""

def isprime(n):
    if n < 2:
        return False
    if n == 2 or n==3:
        return True
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True
from math import sqrt
def isprime2(n):
    if n < 2:
        return False
    if n == 2 or n==3:
        return True
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False
    return True


low, high = list(map(int, input().split(",")))
primes = []

for i in range(low, high+1):
    if isprime(i):
        primes.append(i)

print(primes)





