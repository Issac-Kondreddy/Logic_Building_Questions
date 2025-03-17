def equalnumbers(arr, n):
    for i in range(0, n):
        while arr[i]%2==0:
            arr[i]//=2
        while arr[i]%3==0:
            arr[i]//=3
        if arr[i]!=arr[0]:
            return False
    return True
arr1 = [50,75,100]
print(equalnumbers(arr1, len(arr1)))