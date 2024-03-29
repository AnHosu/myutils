def fib(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def fib_nth(n):
    if n <= 1:
        return n
    else:
        return fib_nth(n - 1) + fib_nth(n - 2)

