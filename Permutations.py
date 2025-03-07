"""
n people - r seats - npr - n!/r!*(n-r)!
"""

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def permutations(n, r):
    return factorial(n) / (factorial(n - r))

print(permutations(2, 3))
print(permutations(2, 4))
print(permutations(10, 6))