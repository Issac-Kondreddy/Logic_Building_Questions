def ReplaceByRank(arr):
    temp = arr.copy()
    sorted_array = sort1(temp)
    ranks = {}
    rank_count = 1
    i = 1
    ranks[sorted_array[0]] = rank_count
    for i in range(1, len(sorted_array)):
        if sorted_array[i-1]==sorted_array[i]:
            ranks[sorted_array[i]] = rank_count
        else:
            rank_count += 1
            ranks[sorted_array[i]] = rank_count
        i += 1
    print(ranks)
    for i in range(len(arr)):
        if arr[i]  in ranks:
            arr[i] = ranks[arr[i]]
    return arr

def sort1(arr1):
    for i in range(0, len(arr1)):
        for j in range(0, len(arr1)-i-1):
            if arr1[j]>arr1[j+1]:
                arr1[j],arr1[j+1] = arr1[j+1], arr1[j]
    return arr1


arr = [100, 2, 70, 12 , 90]
print(ReplaceByRank(arr))