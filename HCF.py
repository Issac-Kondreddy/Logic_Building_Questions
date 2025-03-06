def HCF1(a,b):
    if a == b:
        return a
    hcf = 1
    for i in range(1, min(a,b)):
        if a % i == 0 and b % i == 0:
            if i>hcf:
                hcf = i
    return hcf

print(HCF1(36, 60))

def HCF2(a,b):
    while a!=b:
        if a>b:
            a -= b
        else:
            b -= a
    return a

print(HCF2(28, 84))


def HCF3(a,b):
    while b!=0:
        a,b = b, a%b
    return a
print(HCF3(24,48))