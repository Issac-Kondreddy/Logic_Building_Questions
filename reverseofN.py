"""
Reverse a given Number
12345 -> 54321
"""

def reverseofN(num):
    is_neg = num < 0
    num = abs(num)
    rev = 0
    while num>0:
        rem = num % 10
        rev = rem + rev * 10
        num = num // 10
    return -rev if is_neg else rev

num = int(input("Enter a number: "))
print("Using Mathematical Logic: ", reverseofN(num))

def reverseofNstring(num):
    if num < 0:
        return -int(str(abs(num))[::-1])
    return int(str(num)[::-1])
print("Using String Slicing:",reverseofNstring(num))
