def SortArray(arr):
    for i in range(0, len(arr)+1):
        swapped = False
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr



arr = [72,3,7,10,8,2,4,33,41]
print(SortArray(arr))
