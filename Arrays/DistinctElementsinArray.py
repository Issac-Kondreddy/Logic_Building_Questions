def count_distinct_elements(arr):
    dict = {}
    count = 0
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in dict.keys():
        count += 1
    return count

arr = [10, 20, 40, 30, 50, 20, 10, 20]
print(count_distinct_elements(arr))

def count_distinct_elements2(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return len(dict)
print(count_distinct_elements2(arr))