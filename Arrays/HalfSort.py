def SortArray(arr):
    low = 0
    high = len(arr)-1
    mid = (low+high)//2
    leftarr = arr[low:mid+1]
    rightarr = arr[mid+1:]
    leftarrsorted = SortAscending(leftarr)
    rightarraysorted = SortDescending(rightarr)
    return leftarrsorted + rightarraysorted

def SortAscending(arr):
    for i in range(0, len(arr)):
        swapped = False
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            if not swapped:
                break
    return arr
def SortDescending(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [72,3,7,10,8,2,4,33,41]
print(SortArray(arr))