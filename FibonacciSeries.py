"""
fibonaci Series
"""

def FibonacciSeries(n):
    term_1 = 0
    term_2 = 1
    if n == 0:
        return term_1
    fibonacci_series = [term_1, term_2]
    for i in range(2, n):
        next_term = term_1 + term_2
        fibonacci_series.append(next_term)
        term_1 , term_2 = term_2 ,next_term
    return fibonacci_series

n = int(input())
print(FibonacciSeries(n))