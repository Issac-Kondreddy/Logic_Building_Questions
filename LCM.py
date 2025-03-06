def GCD(a, b):
    while b!=0:
        a,b = b, a%b
    return a

def LCM(a, b):
    return (a*b)/GCD(a,b)



def LCM2(a,b):
    for i in range(max(a,b), 1+(a*b)):
        if i%a ==0 and i%b == 0:
            return i
print(LCM(12, 14))
print(LCM2(12, 14))