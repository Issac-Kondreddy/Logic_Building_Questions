def length(n):
    count = 0
    for i in n:
        count += 1
    return count


n = input("Enter the String: ")
print(length(n))


print(len(n))