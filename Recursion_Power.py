# Implement integer exponentiation power(base, exp). Do it with recursion

def power(base, exp):
  # Negative exponent
  if exp < 0:
    return power(1 / base, -1 * exp)
  # Base case
  if exp == 0:
    return 1
  return base * power(base, exp - 1)
