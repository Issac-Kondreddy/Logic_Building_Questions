def reverse(arr, left, right):
    if left==right:
        return arr
    while left<right:
        arr[left], arr[right] = arr[right], arr[left]
        return reverse(arr, left+1, right-1)

def reverse2(arr, left, right):
    while left<right:
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1
    return arr

arr = [1,2,3,4,5]
print(reverse(arr, 0, len(arr)-1))
print(reverse2(arr, 0, len(arr)-1))
