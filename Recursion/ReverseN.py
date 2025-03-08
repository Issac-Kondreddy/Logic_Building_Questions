def ReverseN(n, rev):
    while n>0:
        return ReverseN(n//10, (rev*10+(n%10)))
    return rev
print(ReverseN(123,0))
print(ReverseN(123456,0))
print(ReverseN(5409,0))
