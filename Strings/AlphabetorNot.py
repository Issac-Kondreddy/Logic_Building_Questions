def isAlphabet(n):
    if n >= 'A' and n <='Z':
        return True
    elif n>='a' and n<='z':
        return True
    else:
        return False

n = input("Enter the Char: ")
print(isAlphabet(n))

print(n.isalpha())