
def gcd(x,y):
    while y!=0:
        x, y = y, x % y
    return x

def sumoffractions(num1,den1, num2, den2):
    lcm = (den1*den2)//gcd(den1,den2)
    numerator = ((num1*den2)+(num2*den1))
    denominator = (den1*den2)
    common_Divisor = gcd(numerator,denominator)
    return (numerator//common_Divisor, denominator//common_Divisor)


num1, den1 = map(int, list(input().split()))
num2, den2 = map(int, list(input().split()))
print(sumoffractions(num1, den1, num2, den2))

