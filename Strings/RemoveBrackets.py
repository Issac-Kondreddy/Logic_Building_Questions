def removeBrackets(expr):
    brackets = ['{','}','[',']','(',')']
    output = ""
    for i in expr:
        if i in brackets:
            output += ""
        else:
            output += i
    return output


exp = "(a-b)+[c*d]+{e/f}"
print(removeBrackets(exp))