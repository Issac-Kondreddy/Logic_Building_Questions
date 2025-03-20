def VorC(n):
    if n.isalpha():
        vowels = ['A','E','I','O','U','a','e','i','o','u']
        if n in vowels:
            return "Vowel"
        return "Consonant"
    return "Not an Alphabet"

n = input("Enter the Char : ")
print(VorC(n))