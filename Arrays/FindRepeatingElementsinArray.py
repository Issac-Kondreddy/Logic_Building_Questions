def repeatative_elements(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    res = []
    for key, value in dict.items():
        if value>1:
            res.append(key)
    return res


n = [10, 20, 40, 30, 50, 20, 10, 20]

print(repeatative_elements(n))