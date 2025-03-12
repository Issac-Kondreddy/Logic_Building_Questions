arr = [34,54,2,3,4,22,78,-1]

#Method 1
def Smallest1(arr):
    return min(arr)

#Method 2
def smallest2(arr):
    low = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < low:
            low = arr[i]
    return low

def smallest3(arr):
    arr.sort()
    return arr[0]

def smallest4(arr,n):
    if n==1:
        return arr[0]
    else:
        return min(arr[n-1], smallest4(arr, n-1))
print(Smallest1(arr))
print(smallest2(arr))
print(smallest3(arr))
print(smallest4(arr,len(arr)))
