def lengthOfString(s,n=0):
    if s=="":
        return n
    return lengthOfString(s[1:],n+1)

print(lengthOfString("issac"))
print(lengthOfString(""))
print(lengthOfString("i"))
print(lengthOfString("Issac Kondreddy"))