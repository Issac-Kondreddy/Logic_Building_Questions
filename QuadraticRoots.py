import math
def roots(a,b,c):
    d = (b*b)-(4*a*c)
    if d>0:
        print("Roots are real and different")
        return (-b+math.sqrt(d))/(2*a), (-b-math.sqrt(d))/(2*a)
    elif d==0:
        print("Roots are real and Same")
        return -b/(2*a)
    else:
        print("Roots are imaginary")
        print(-b/(2*a) , " +i" , d)
        print(-b/(2*a), " -i" , d)
        return

print(roots(1,4,4))
print(roots(1, -2, -15))
