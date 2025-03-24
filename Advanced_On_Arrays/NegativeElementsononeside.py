def NegativetoOneSide(arr):
    arr.sort()
    return arr

array= [1, 3, -1, 4, -3, -5, -6, 3, 7]
print(NegativetoOneSide(array))


def WithoutSort(arr):
    n = len(arr)
    j = 0
    for i in range(n):
        if arr[i]<0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

array= [1, 3, -1, 4, -3, -5, -6, 3, 7]
print(WithoutSort(array))