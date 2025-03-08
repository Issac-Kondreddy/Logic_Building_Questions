number = int(input("Enter the number: "))
digit = int(input("Enter the digit: "))
num = list(str(number))
count = 0
for i in range(len(num)):
    if num[i] == str(digit):
        count += 1
print(count)


def countOccurence(num, d):
    count = 0
    while num>0:
        if (num%10==d):
            count += 1
        num = num//10
    return count

print(countOccurence(number,digit))