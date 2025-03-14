def remoduplication(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    return res
arr = [10, 20, 20, 30, 40, 40, 40, 50, 50]
print(remoduplication(arr))

def remoduplication2(arr):
    return list(sorted(set(arr)))

print(remoduplication2(arr))