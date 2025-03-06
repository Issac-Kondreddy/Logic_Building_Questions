bin = int(input())
total = 0
base = 1
bin_array = list(map(int, str(bin)))
length = len(bin_array)
for i in range(length-1, -1, -1):
    digit = bin_array[i]
    total = total + digit*base
    base *= 2
print(total)
