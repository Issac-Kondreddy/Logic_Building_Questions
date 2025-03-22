

def get_permutations(string, i = 0):
    if i==0:
        string = sorted(string)
    if i == len(string):
        print("".join(string), end = " ")
    for j in range(i, len(string)):
        words = [char for char in string]
        if i!=j and words[i]==words[j]:
            continue
        words[i], words[j] = words[j], words[i]
        get_permutations(words, i+1)

str1 = "cga"
print(get_permutations(str1))