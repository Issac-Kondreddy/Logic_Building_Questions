def isAutomorphicNumber(n):
    sqaured = n*n
    count = countdigits(n)
    reconstruction = 0
    while count>0:
        rem = sqaured % 10
        reconstruction = (reconstruction * 10) + rem
        sqaured = sqaured // 10
        count -= 1
    corrected_reconstruction = 0
    while reconstruction > 0:
        rem = reconstruction % 10
        corrected_reconstruction = (corrected_reconstruction * 10) + rem
        reconstruction //= 10
    return corrected_reconstruction == n



def countdigits(m):
    count = 0
    while m>0:
        count += 1
        m = m//10
    return count

def isAutomorphic2(n):
    squared = n*n
    count = countdigits(n)
    return n == squared%(10**count)

# for i in range(1,10000):
#     if isAutomorphicNumber(i):
#         print(f"{i} is a Automorphic number")

for i in range(1,1000):
    if isAutomorphic2(i):
        print(f"{i} is a Automorphic number")