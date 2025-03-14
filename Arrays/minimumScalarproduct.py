def minimumScalarproduct(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    arr1.sort()
    arr2.sort(reverse=True)
    i, j,product= 0,0,0
    while i < n1 and j < n2:
        product += arr1[i] * arr2[j]
        i += 1
        j += 1
    return product
arr1 = [1, 2, 6, 3, 7]
arr2 = [10, 7, 45, 3, 7]
print(minimumScalarproduct(arr1, arr2))
