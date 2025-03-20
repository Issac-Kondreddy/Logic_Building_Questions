def RemoveSpaces(str):
    output = ""
    for i in str:
        if i == " ":
            output += ""
        else:
            output += i
    return output

str = "    Issac Kondreddy!"
print(str)
print(RemoveSpaces(str))
