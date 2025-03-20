def frequency(str):
    str = str.lower()
    freq = {}
    for i in str:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    output = ""
    for k, v in freq.items():
        if v==1:
            output += k
        output += " "
    return output


str = "prepinsta"
print(frequency(str))