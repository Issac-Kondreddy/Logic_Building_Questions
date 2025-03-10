def max_num(array, n):
    if n==1:
        return array[0]
    return max(array[n-1], max_num(array, n-1))

array = [3,4,2,5,45,6,44,67,12,43]
n = len(array)
print(max_num(array, n))
