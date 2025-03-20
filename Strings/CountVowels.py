def CountVowels(str):
    vowels = ['a','e','i','o','u']
    str = str.lower()
    count = 0
    for i in str:
        if i in vowels:
            count += 1
    return count

str = input("Enter the String: ")
print(CountVowels(str))