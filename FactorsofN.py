"""
Factors of N
"""
import math
n = int(input("Enter the value of n: "))
for i in range(1, n+1):
    if n%i==0:
        print(f"{i}", end = " ")
print()

for i in range(1, int(math.sqrt(n))+1):
    if n%i==0:
        if n/i==i:
            print(f"{i}")
        else:
            print(f"{i} and {int(n/i)}")


