"""
https://www.geeksforgeeks.org/memoization-using-decorators-in-python/
"""

from time import perf_counter

def fib(n):
    print(f"computing fib({n})")
    if n == 0:
        print("returning 0")
        return 0
    elif n == 1:
        print("returning 1")
        return 1
    else:        
        return fib(n-1) + fib(n-2)

n = 20

start_time = perf_counter()
a1 = fib(n)
stop_time = perf_counter()
run_time = stop_time - start_time
print(f"fib({n}) = {a1}")
print(f"Duration of regular fib: {1000*run_time:.3f} milliseconds")


def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    
fib = memoize(fib)

start_time = perf_counter()
a2 = fib(n)
stop_time = perf_counter()
run_time = stop_time - start_time
print(f"fib({n}) = {a2}")
print(f"Duration of memoized fib: {1000*run_time:.3f} milliseconds")
