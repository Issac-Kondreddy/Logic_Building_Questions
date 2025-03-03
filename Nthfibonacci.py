def fibonacci(n):
    global next_term
    term_1, term_2 = 0,1
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for _ in range(1, n):
            next_term = term_1 + term_2
            term_1, term_2 = term_2, next_term
        return next_term

n = int(input())
print(fibonacci(n))


def fibo_recursion(n):
    if n <= 1:
        return n
    return fibo_recursion(n-1) + fibo_recursion(n-2)

print(fibo_recursion(n))