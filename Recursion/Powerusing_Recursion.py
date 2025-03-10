def Power_Recursion(base, power):
    if power == 0 and base ==0:
        return "Not Defined"
    if power==0:
        return 1
    return base * Power_Recursion(base, power-1)

print(Power_Recursion(2,3))
print(Power_Recursion(2,4))
print(Power_Recursion(5,2))
print(Power_Recursion(5,0))
print(Power_Recursion(0,0))