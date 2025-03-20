def RemoveSplChars(str):
    output = ""
    for i in str:
        if not i.isalpha():
            i = ""
            output += i
        else:
            output += i
    return output

str = "Iss@c Kondreddy!"
print(RemoveSplChars(str))