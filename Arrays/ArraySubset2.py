def subsetusingsorting(A,B):
    if len(A)==0:
        return True
    if len(B)==0 and len(A)==0:
        return True
    if len(B)==0 and len(A)!=0:
        return False
    A.sort()
    B.sort()
    i = 0
    j = 0
    while i<len(A) and j < len(B):
        if A[i]<B[j]:
            return False
        elif A[i]==B[j]:
            i += 1
        j += 1
    return i == len(A)

A = [4,5]
B = [1,2,3,4,5,6,7]
print(subsetusingsorting(A,B))

