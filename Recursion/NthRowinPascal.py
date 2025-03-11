def pascal(n):
    for row in range(n):
        coef = 1
        print(" " * (n-row), end="")
        for col in range(row+1):
            print(coef, end=" ")
            coef = coef * (row-col)//(col+1)
        print()

pascal(5)

def get_pascal_row(n):
    row = [1]
    prev = 1
    for k in range(1, n+1):
        next_elem = (prev*(n-k+1))//k
        row.append(next_elem)
        prev = next_elem
    return row

print(get_pascal_row(1))
print(get_pascal_row(2))
print(get_pascal_row(3))
print(get_pascal_row(4))
print(get_pascal_row(5))


def getrow(rowIndex):
    curr_row = []
    curr_row.append(1)
    if rowIndex == 0:
        return curr_row
    prev = getrow(rowIndex-1)
    for i in range(1, len(prev)):
        curr = prev[i-1]+prev[i]
        curr_row.append(curr)
    curr_row.append(1)
    return curr_row

print(getrow(1))
print(getrow(2))
print(getrow(3))