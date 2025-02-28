"""
Check Whether a Number is Even or Odd in Python
Given an integer input the objective is to write a
Python code to Check Whether a Number is Even or Odd.
"""

def even_odd(n):
    if n%2==0:
        return True
    return False


print(even_odd(5))
print(even_odd(4))

n = 4
print("Even" if n%2==0 else "Odd")

#Bitwise Method

print("Even" if n&1==0 else "Odd")