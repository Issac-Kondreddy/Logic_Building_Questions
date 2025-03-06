Hex_decimal = input("Enter the decimal number: ")
hex_array = list(map(str, str(Hex_decimal)))
length = len(hex_array)
total = 0
base = 1
for i in range(length-1, -1, -1):
    digit = hex_array[i]
    if digit>="0" and digit<="9":
        digit = ord(digit) - ord('0')
    elif digit>="A" and digit<="F":
        digit = ord(digit) - ord('A') + 10
    elif digit>="a" and digit <= "f":
        digit = ord(digit) - ord('a') + 10
    else:
        print("Error")
    total = total + digit*base
    base *= 16
print(total)