def Anagrams(str1,str2):
    if len(str1)==len(str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    return False

str1 = "Triangle"
str2 = "integral"
print(Anagrams(str1, str2))
str3 = "cinema"
str4 = "iceman"
print(Anagrams(str3, str4))


#Method 2
def Anagrams_2(str1, str2):
    if len(str1)!=len(str2):
        return False
    str1 = str1.lower()
    str2 = str2.lower()
    str1_hash = {}
    str2_hash = {}
    for i in str1:
        if i in str1_hash:
            str1_hash[i] += 1
        else:
            str1_hash[i] = 1
        if i in str2_hash:
            str2_hash[i] += 1
        else:
            str2_hash[i] = 1
    return str1_hash == str2_hash


str1 = "Triangle"
str2 = "integral"
print(Anagrams_2(str1, str2))
str3 = "cinema"
str4 = "iceman"
print(Anagrams_2(str3, str4))
