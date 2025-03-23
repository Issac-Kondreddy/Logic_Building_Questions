def sort(arr):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for i in arr:
        if i == 0:
            count_0 += 1
        elif i==1:
            count_1 += 1
        else:
            count_2 += 1
    res = []
    for i in range(count_0):
        res.append(0)
    for i in range(count_1):
        res.append(1)
    for i in range(count_2):
        res.append(2)
    return res


#Method 2
def optimizedsort(arr):
    low = 0
    current = 0
    high = len(arr)-1
    while current<=high:
        if arr[current]==0:
            arr[low], arr[current] = arr[current], arr[low]
            low += 1
            current += 1
        elif arr[current]==1:
            current += 1
        else:
            arr[high], arr[current] = arr[current], arr[high]
            high -= 1
    return arr



arr = [0,1,1,2,0,0,2,1,1,0,0]
print(sort(arr))
print(optimizedsort(arr))
