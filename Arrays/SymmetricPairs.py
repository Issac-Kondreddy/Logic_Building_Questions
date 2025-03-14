def SymmetricPairs(arr):
    hashmap = {}
    for i in range(0, len(arr)):
            if arr[i][1] in hashmap:
                if hashmap[arr[i][1]] == arr[i][0]:
                    print(f"{arr[i][0], arr[i][1]} are symmetric pair")
            else:
                hashmap[arr[i][0]] = arr[i][1]

arr = [(1, 2), (3, 5), (4, 6), (5, 3), (2, 1), (6, 4)]
SymmetricPairs(arr)