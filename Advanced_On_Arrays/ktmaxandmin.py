def KthMaxMin(arr,k):
    arr1 = sorted(arr)
    print(f"{k} max is : {arr1[len(arr)-k]}")
    print(f"{k} min is : {arr1[k-1]}")

arr = [7,10,1,3,4,20,15, 36,49]
KthMaxMin(arr, 3)