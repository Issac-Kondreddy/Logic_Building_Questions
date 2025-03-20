def frequency(str):
    str = str.lower()
    freq = {}
    for i in str:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq


str = "Yolo Life"
print(frequency(str))