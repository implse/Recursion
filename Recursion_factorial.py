# Recursive factorial
def factorial(n):
    if n == 0:
        return 1 # Base case
    return n * factorial(n - 1) # Break into smaller problem(s)


# Iterative factorial
def factorial(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
    return product
