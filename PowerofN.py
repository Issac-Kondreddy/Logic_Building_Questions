"""
Given two integers n, m
return the power of n to m
"""

def power(n, m):
    if m==0:
        return 1
    if m==1:
        return n
    return n * pow(n, m-1)

n = int(input("Enter the Base n: "))
m = int(input("Enter the Power m: "))
print(power(n, m))

#Method 2
powered = 1
for i in range(1, m+1):
    powered *= n

print(powered)


#method 3
import math
print(math.pow(n,m))