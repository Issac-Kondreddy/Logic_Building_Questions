"""
              *
             ***
            *****
           *******
"""

n = int(input())
for i in range(n):
    for j in range(2*n-1):
        if n-i-1 <= j and j<=n-1+i:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()