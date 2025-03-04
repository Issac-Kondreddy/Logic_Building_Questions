n = int(input("Enter the N for Prime Factors:  "))
print(f"Prime Factors of {n}: ", end= " ")
i = 2
primefactors = []
while n>1:
    if n % i == 0:
        primefactors.append(i)
        n //= i
    else:
        i += 1 if i == 2 else 2
print(primefactors)
