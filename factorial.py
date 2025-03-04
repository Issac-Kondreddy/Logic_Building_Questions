"""
Factorial of given number
"""
n = int(input())
def factorial_recursion(n):
    if n==0 or n==1:
        return 1
    return n * factorial_recursion(n-1)



for i in range(1,n+1):
    print(f"{i} -> {factorial_recursion(i)}")

# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)