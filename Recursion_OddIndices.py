# Write a recursive function that prints out the odd indices of an integer.

# Simple Solution
def indices_A(arr, i):
  # Base case
  if len(arr) == i:
    return
  # Recursive case
  if i % 2 != 0:
    print(arr[i])
  indices_A(arr, i+1)

# Optimize Solution - reduce recursive calls
def indices_B(arr, i):
  # Base case
  if i >= len(arr):
    return
  # Recursive case
  print(arr[i])
  indices_B(arr, i+2)

# Test
a = [2, 4, 6, 8, 10, 12]

# Indices A
indices_A(a, 0)
# Indices B start i = 1
indices_B(a, 1)
