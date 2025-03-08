def count_digits(num):
    count = 0
    while num!=0:
        count += 1
        num = num//10
    return count
import math
def count_digits2(num):
    if num<0:
        return math.floor(math.log10(abs(num)))+1
    return math.floor(math.log10(num))+1
def count_digits3(num):
    return len(str(num))

print(count_digits(9))
print(count_digits(10))
print(count_digits(112200))
print(count_digits(12345))
print(count_digits2(123453))
print(count_digits3(12345))
print(count_digits2(-12345))