def disjoint(arr1, arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)
    set1 = arr1.intersection(arr2)
    if set1:
        return "Arrays are not disjoint"
    return "Arrays are disjoint"

arr1 = [1,2,3]
arr2 = [4,5,7]
print(disjoint(arr1,arr2))


def disjoint2(arr1, arr2):
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            if arr1[i] == arr2[j]:
                return "Arrays are not disjoint"
    return "Arrays are disjoint"

print(disjoint2(arr1,arr2))