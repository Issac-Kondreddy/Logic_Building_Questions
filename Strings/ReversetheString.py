def ReverseString1(str):
    return str[::-1]

def ReverseString2(str):
    output = ""
    for i in str[::-1]:
        output += i
    return output


str = "Issac Kondreddy"
print(ReverseString1(str))
print(ReverseString2(str))
