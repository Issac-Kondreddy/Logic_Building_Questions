def permutation(str, left, right):
    if left==right:
        print(str)
    else:
        for i in range(left, right+1):
            string = swap(str, left, i)
            permutation(string, left+1, right)
            string = swap(string, left, i)


def swap(str, i, j):
    s = list(str)
    s[i], s[j] = s[j], s[i]
    return "".join(s)

print(permutation("ABCD", 0, 3))