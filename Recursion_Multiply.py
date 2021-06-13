# Given two numbers, find their product using recursion

# Recursive Solution
def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    # base case
    if y == 1:
        return x 
    return x + multiply(x, y - 1)

# Recursive Solution where x < y to minimize the number of recursive calls.
def multiply(x, y):
    if x < y:
        return multiply(y, x)
    if x == 0 or y == 0:
        return 0
    if y == 1:
        return x
    return x + multiply(x, y - 1)

# Test
print(multiply(3, 4))
print(multiply(200, 500))
print(multiply(1, 0))



