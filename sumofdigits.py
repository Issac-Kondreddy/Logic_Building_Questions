"""
Sum of digits in a given Number
"""

n = int(input())
res = 0
while n>0:
    rem = n%10
    res += rem
    n = n // 10

print(res)


def sumDigits(n):
    if n == 0:
        return 0
    while n>0:
        return n%10 + sumDigits(n//10)

print(sumDigits(1234))