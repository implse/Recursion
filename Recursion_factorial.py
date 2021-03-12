# Factorial Recursive
def factorial(n):
    if n == 0:
        return 1 # Base case
    return n * factorial(n - 1) # Break into smaller problem(s)


# Factorial Memoization
def factorial_memo(n):
    memo = dict()
    def factorial(n):
        if n == 0:
            return 1
        if n in memo.keys():
            return memo[n]
        return n * factorial(n - 1)
    return factorial(n)


# Factorial Iterative
def factorial_iterative(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
    return product

print(factorial(10))
print(factorial_memo(10))
print(factorial_iterative(10))
