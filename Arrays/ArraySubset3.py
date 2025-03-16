def subsetusingHashing(A, B):
    hashtable = countoccur(B)
    for i in A:
        if i in hashtable and hashtable[i] > 0:
            hashtable[i] -= 1
        else:
            return False
    return True
def countoccur(B):
    dict1 = {}
    for i in B:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1


A = [4,3]
B = [1,2,3,4,5,6,7]
print(subsetusingHashing(A,B))