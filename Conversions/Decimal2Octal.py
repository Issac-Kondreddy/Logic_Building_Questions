decimal = int(input("Enter the decimal number: "))
oct_array = []
while decimal > 0:
    rem = decimal % 8
    oct_array.append(rem)
    decimal = decimal // 8
for j in range(len(oct_array)-1, -1, -1):
    print(oct_array[j], end="")