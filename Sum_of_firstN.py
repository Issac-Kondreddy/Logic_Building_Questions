"""
Find the Sum of the First N Natural Numbers in Python
Given an integer input of N, the objective is to find the sum of all the natural numbers until the given input integer
"""
#Method 1
n = int(input())
res = 0
for i in range(n+1):
    res += i

print(res)

#Method 2
def sumofN(n):
    if n==0 or n==1:
        return n
    return n + sumofN(n-1)

print(sumofN(10))


#Method 3
print((n*(n+1))/2)