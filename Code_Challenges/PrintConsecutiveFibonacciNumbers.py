from functools import cache


def fib1(n):
    a = 0
    b = 1
    while a <= n:
        print(a)
        c = a + b
        a, b = b, c


fib1(10)


@cache
def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib2(n-1) + fib2(n-2)


print(fib2(10))
