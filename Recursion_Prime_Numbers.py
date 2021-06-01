# Given an integer n, write a recursive function that return True if n is a prime number otherwise return False.else

# A prime number is a number that is divisible only by itself and 1.


# Recursive fucntion
def is_Prime(n, i=2):
    if i == n:
        return True
    elif n % i == 0 or n <= 1:
        return False
    else:
        return is_Prime(n, i + 1)


list_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]


for num in range(72):
    if is_Prime(num, i=2) == True:
        print(f'{num} is prime.')
    else:
        print(f'{num} is not prime')


# Iterative
def is_Prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for num in range(72):
    if is_Prime(num) == True:
        print(f'{num} is prime.')
    else:
        print(f'{num} is not prime')

