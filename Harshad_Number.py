def isHarshad(n):
    sum_of_n = 0
    temp = n
    while temp > 0 :
        sum_of_n += temp%10
        temp = temp // 10
    return True if n%sum_of_n == 0 else False

for i in range(1, 100):
    if isHarshad(i):
        print(f"{i} is Harshad Number")