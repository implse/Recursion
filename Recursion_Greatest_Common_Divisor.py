# Find the Greatest Common Divisor of two numbers
# The Greatest Common Divisor (GCD) of two numbers a and b is the largest number
# that divides a and b without leaving a remainder.
# For instance, the GCD of 12 and 20 is 4. It is also called Greatest Common Factor, Highest Common Factor.


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, (a % b))

print(gcd(12, 20)) # 4
print(gcd(128, 12)) # 4
