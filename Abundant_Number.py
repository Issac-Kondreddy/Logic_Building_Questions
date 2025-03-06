def isAbundantNumber(n):
    factors = [i for i in range(1, n) if n%i==0]
    sum_of_factors = sum(set(factors))
    if sum_of_factors > n:
        return True
    return False

print(isAbundantNumber(120))
