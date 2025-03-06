decimal = int(input("Enter the decimal number: "))
hexa_array = []
while decimal > 0:
    rem = decimal % 16
    if rem>=0 and rem<=9:
        hexa_array.append(chr(rem+48))
    else:
        hexa_array.append(chr(rem+55))
    decimal = decimal // 16

for j in range(len(hexa_array)-1, -1, -1):
    print(hexa_array[j], end="")
