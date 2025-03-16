def subsetbruteforce(A, B):
    if len(A)==0:
        return True
    if len(B)==0 and len(A)==0:
        return True
    if len(B)==0 and len(A)!=0:
        return False
    for i in A:
        found = False
        for j in B:
            if i==j:
                found = True
                break
        if not found:
            return False
    return True

A = [4,5,7]
B = [1,2,3,4,5,6,7]
print(subsetbruteforce(A,B))

