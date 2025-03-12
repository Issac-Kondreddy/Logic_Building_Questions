xf
# def secsmall(arr):
#     arr.sort()
#     return arr[1]
# print(secsmall(arr))

def secsmall2(arr):
    low = arr[0]
    second = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < low:
            second = low
            low = arr[i]
        if low < arr[i] < second:
            second = arr[i]
    return second


print(secsmall2(arr))