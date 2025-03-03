"""
Palindrome Number:
121 -> True
123 -> False
"""

def Palindrome(num):
    if num < 0:
        return False
    temp = num
    rev = 0
    while temp > 0:
        rem = temp % 10
        rev = (rev*10) + rem
        temp = temp // 10
    return True if num == rev else False

num = int(input("Enter a number: "))
if Palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")


def PalindromStringMethod(num):
    if num == int(str(num)[::-1]):
        return "Palindrome"
    else:
        return "Not Palindrome"

print("Using String Method:",PalindromStringMethod(num))