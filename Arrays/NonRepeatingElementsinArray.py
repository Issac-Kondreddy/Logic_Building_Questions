def non_repeatative_elements(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    res = []
    for key, value in dict.items():
        if value==1:
            res.append(key)
    return res

arr = [10, 20, 70, 90, 80, 20, 10, 20]
print(non_repeatative_elements(arr))