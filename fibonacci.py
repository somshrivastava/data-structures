# highly inefficient method, O(2^n)
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

# highly efficient method, O(2n-1)
memo = [None] * 100
def fib2(n):
    if memo[n] is not None:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]

# bottom up, O(n-1)
def fib3(n):
    fib_list = [0, 1]
    for i in range(2, n+1):
        next_fib = fib_list[i-1] + fib_list[i-2]
        fib_list.append(next_fib)
    return fib_list[n]