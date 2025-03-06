octal_num = int(input("Enter Octal Number: "))
octal_array = list(map(int, str(octal_num)))
length = len(octal_array)
base = 1
total = 0
for i in range(length-1, -1, -1):
    digit = octal_array[i]
    total = total + digit*base
    base *= 8
print(total)
