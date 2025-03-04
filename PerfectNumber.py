"""
Perfect Number - if sum of divisors of the number is equal to itself
28 = [1,2,7,14]
sum([1,2,7,14]) = 28
"""

n = int(input())
list=[]
for i in range(1,n):
    if n%i==0:
        list.append(i)
if n == sum(list):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")