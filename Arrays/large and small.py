arr = [34,54,2,3,4,22,78,-1]

low = arr[0]
high = arr[0]
for i in range(1, len(arr)):
    if arr[i]>high:
        high = arr[i]
    elif arr[i]<low:
        low = arr[i]
print(high)
print(low)