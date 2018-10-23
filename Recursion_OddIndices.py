# Write a recursive function that prints out the odd indices of an integer.

def indices(arr, i):
  # Base case
  if len(arr) == i:
    return
  # Recursive case
  if i % 2 != 0:
    print(arr[i])
  indices(arr, i+1)

# Test
a = [2, 4, 6, 8, 10, 12]
indices(a, 0)
