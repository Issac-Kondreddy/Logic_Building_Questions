arr = [34,54,2,3,4,22,78,-1]

#Method 1
def largest1(arr):
    return max(arr)

#Method 2
def largest2(arr):
    large = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > large:
            large = arr[i]
    return large

def largest3(arr):
    arr.sort()
    return arr[len(arr)-1]

print(largest1(arr))
print(largest2(arr))
print(largest3(arr))