def Toggle(str):
    output = ""
    for i in str:
        if i.islower():
             i = i.upper()
             output += i
        else:
            i = i.lower()
            output += i
    return output

str = "IsSaC KonDreddY"
print(Toggle(str))
print(str.swapcase())