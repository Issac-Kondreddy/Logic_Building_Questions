def HCF(n, x):
    while x!=0:
        return HCF(x, n%x)
    return n

print(HCF(23, 69))
print(HCF(24,48))
print(HCF(36, 60))