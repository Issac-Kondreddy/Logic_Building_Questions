"""
******
******
******
******
"""

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of cols: "))
for i in range(rows):
    for j in range(cols):
        print("*", end = " ")
    print()