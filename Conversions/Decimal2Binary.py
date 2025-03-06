decimal = int(input("Enter the decimal number: "))
bin_array = []
while decimal > 0:
    rem = decimal % 2
    bin_array.append(rem)
    decimal = decimal // 2
for j in range(len(bin_array)-1, -1, -1):
    print(bin_array[j], end="")
