"""
*
* *
* * *
* * * *
* * *
* *
*
"""

n = int(input("Enter the input: "))
for i in range(n):
    if i>=n//2:
        for j in range(n, i, -1):
            print("*", end = " ")
        print()
    else:
        for j in range(i+1):
            print("*", end = " ")
        print()