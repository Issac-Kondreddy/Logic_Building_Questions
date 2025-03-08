number = int(input("Enter the number: "))
d = int(input("Enter the divisor: "))

count = 0
for i in range(1, number + 1):
    count_factors = 0
    for j in range(1, i+1):
        if i % j == 0:
            count_factors += 1
    if count_factors == d:
        count += 1


print(count)
