def countFrequency(arr):
    frequency = {}
    for i in range(0, len(arr)):
        if arr[i] not in frequency.keys():
            frequency[arr[i]] = 1
        else:
            frequency[arr[i]] += 1
    return frequency

arr = [10,20,30,20,30,10,20,30,10]
print(countFrequency(arr))