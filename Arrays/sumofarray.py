def sumofarray(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

def sumofarray2(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sumofarray(arr[1:])

arr = [34,54,2,3,4,22,78,-1]
print(sumofarray(arr))
print(sumofarray2(arr))
print(sum(arr))