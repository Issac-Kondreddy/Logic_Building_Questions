def minimumsum(arr, n):
    result = 0
    for i in range(0, n):
        min_diff = float('inf')
        for j in range(0, n):
            if i!=j:
                min_diff = min(min_diff, abs(arr[i]-arr[j]))
        result = result + min_diff
    return result

arr = [1,4,5]
print(minimumsum(arr, len(arr)))



