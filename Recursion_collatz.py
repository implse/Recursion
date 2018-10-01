# The collatz conjecture is applies to positive integers and speculates that is
# always possible to get back to 1 if you follow these steps:
#     - If n is 1, stop
#     - Otherwise, if n is even, repeat this process on n/2
#     - Otherwise, if n is odd, repeat this process on 3n + 1


# Write a recursive function collatz(n) that calculates how many steps it takes to get
# to 1 if you start from n and recurse as indicated above.

def collatz(n):
    # Base case
    if n == 1:
        return 0
    # Even numbers
    elif n % 2 == 0:
        return 1 + collatz(n/2)
    # Odd numbers
    else:
        return 1 + collatz(3*n + 1)
