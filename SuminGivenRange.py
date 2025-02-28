"""
Sum of numbers in Given Range
"""
i = int(input("Enter the lowest number range: "))
j = int(input("Enter the highest number range: "))
res = 0
for k in range(i, j+1):
    res += k
print(res)


#Using Recursion
def sumofNinRange(l, h):
    if l==h:
        return l
    return l + sumofNinRange(l+1, h)
print(sumofNinRange(4, 44))
print(sumofNinRange(1, 10))