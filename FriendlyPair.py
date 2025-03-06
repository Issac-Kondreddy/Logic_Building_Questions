import math

def sum_of_factors(n):
    factors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            if i != n // i and n // i != n:
                factors.add(n // i)
    return sum(factors)  # Sum all unique proper divisors

def friendly_pair(n, m):
    if n != m:  # Avoid trivial pair (n == m)
        factors_sum_of_n = sum_of_factors(n)
        factors_sum_of_m = sum_of_factors(m)
        return (n // factors_sum_of_n) == (m // factors_sum_of_m)

for i in range(1, 100):
    for j in range(1, 100):
        if friendly_pair(i, j):
            print(i, j)
