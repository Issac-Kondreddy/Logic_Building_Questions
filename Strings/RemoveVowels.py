def removeVowels(str):
    output = ""
    str = str.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in str:
        if i in vowels:
            output+= ""
        else:
            output += i
    return output

str = input("Enter the String : ")
print(removeVowels(str))