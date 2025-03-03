def Countdigits(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count

def ArmstrongNumber(num):
    power  = Countdigits(num)
    total = 0
    temp = num
    while temp > 0:
        rem = temp % 10
        total +=  rem ** power
        temp = temp // 10
    return total==num

ArmstrongNumbers = []
for i in range(1, 100000):
    if ArmstrongNumber(i):
        ArmstrongNumbers.append(i)

print(ArmstrongNumbers)