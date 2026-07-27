'''Fiaboniceeseries
# 0 1 1 2 3 5 8 13

fib(0) = 0
fib(1) = 1
fib(2) = fib(1) + fib(0)
fib(3) = fib(2) + fib(1)
fib(n) = fib(n-1) + fib(n-2) for n > 2'''

def fib(n):
    if n <= 1:
        return n
    else:
        #best way to solve this problem is using recursion
        return fib(n-1) + fib(n-2)
print(fib(6))