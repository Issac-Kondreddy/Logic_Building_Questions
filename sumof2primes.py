n = int(input())
flag = 0
def sum_of_two_primes(n):
    for i in range(2, n//2):
        if n % i == 0:
            return 0
    return 1

for i in range(2, n//2):
    n1= sum_of_two_primes(i)
    n2 = sum_of_two_primes(n-i)
    if n1==1 and n2==1:
        flag += 1
        print(f"{i} and {n-i}")
if flag == 0:
    print("Not possible")

