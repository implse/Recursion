# Write a recursive algorithm to perform multiplication of positive integers using repeated addition

# 3*3 = 3 + 3 + 3 = 9
# 3*6 = 6 + 6 + 6

def multiply_recursive(a, b):
  if b == 0:
    return 0
  else:
    return a + multiply_recursive(a, b - 1)

print(pmultiply_recursive(3, 3))
print(multiply_recursive(6, 3))
