def count_common_subsequences(str1, str2):
    return count_common(str1, str2, len(str1), len(str2))

def count_common(str1, str2, i, j):
    if i==0 or j == 0:
        return 1
    if str1[i-1] == str2[j-1]:
        return count_common(str1, str2, i-1,j)+count_common(str1,str2, i, j-1)
    return count_common(str1, str2, i, j-1) + count_common(str1, str2, i-1, j) - count_common(str1, str2, i-1, j-1)

str1 = "abc"
str2 = "ac"
print(count_common_subsequences(str1, str2))