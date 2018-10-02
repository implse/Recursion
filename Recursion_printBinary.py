# Print the given integer's in binary representation.
# 43 -> 101011

def printBinary(n):
  # Negative number
  if n < 0:
    print("-", end="")
    printBinary(n * -1)
  # Base case
  elif n < 2:
    print(n, end="")
  # Recursive case
  else:
    lastDigit = n % 2
    restOfDigits = n // 2
    printBinary(restOfDigits)
    print(lastDigit, end="")
