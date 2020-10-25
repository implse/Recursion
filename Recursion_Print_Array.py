# Recursively print all the elements in an array. Write a functions to print the array in order and reverse order.

# Print In Order Recursive
def printInOrder(arr, index):
    # Base case
    if index == len(arr):
      return
    # Recursive case
    print(arr[index])
    printInOrder(arr, index+1)

# Print In Reverse Recursive
def printInReverse(arr, index):
    # Base case
    if index == len(arr):
      return
    # Recursive case
    printInOrder(arr, index+1)
    print(arr[index])


# Test
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(printInOrder(a, 0))
print(printInReverse(a, 0))
