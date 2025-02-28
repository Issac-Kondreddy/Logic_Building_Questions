"""
Check if a Number is Positive and Negative in Python
Given an integer input, the objective is check whether the given integer is Positive or Negative. In order to do so we have the following method,

 Method 1: Using Brute Force
Method 2: Using Nested if-else Statements
Method 3: Using ternary operator
"""

#Method 1
n  = int(input())
if n < 0:
    print("Negative")
elif n==0:
    print("Zero")
else:
    print("Positive")

#Method 2

if n>=0:
    if n==0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")

#Method 3
print("Positive" if n>0 else "Negative")