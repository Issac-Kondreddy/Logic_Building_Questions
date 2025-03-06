"""
Perfect Square
"""
import math
def isPerfectSquare(n):
    if n==1:
        return True
    else:
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                if n // i == i:
                    return True
    return False


for i in range(1, 1000):
    if isPerfectSquare(i):
        print(f"{i} is a perfect square number")