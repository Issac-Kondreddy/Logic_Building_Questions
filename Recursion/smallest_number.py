def smallest_number(array, n):
    if n==1:
        return array[0]
    return min(array[n-1], smallest_number(array, n-1))

array = [3,4,2,5,45,6,44,67,12,43]
n = len(array)
print(smallest_number(array, n))