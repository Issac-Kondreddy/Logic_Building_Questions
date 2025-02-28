num = int(input("Enter a number: "))
import math
def prime(num):
    if num==2 or num==3:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

def primeoptimized(num):
    if num==2 or num==3:
        return True
    else:
        for i in range(2, int(math.sqrt(num))):
            if num % i == 0:
                return False
    return True

# for i in range(2,num+1):
#     if prime(i):
#         print(i ,"is a prime number")
#     else:
#         continue



for i in range(2,num+1):
    if primeoptimized(i):
        print(i ,"is a prime number")
    else:
        continue