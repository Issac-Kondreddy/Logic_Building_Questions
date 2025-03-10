def isPrime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    checkPrime = isPrimeHelper(n, 2)
    if checkPrime:
        return True
    return False

def isPrimeHelper(n, i):
    if i > n/2:
        return True
    while i<n/2:
        if n%i==0:
            return False
        return isPrimeHelper(n, i+1)

for i in range(1, 101):
    if isPrime(i):
        print(i, end = " ")

print()



def isPrime2(n, i=2):
    if i>n/2:
        return True
    if n==i:
        return True
    elif n%i==0:
        return False
    return isPrime2(n, i+1)

for i in range(2, 101):
    if isPrime2(i):
        print(i, end = " ")