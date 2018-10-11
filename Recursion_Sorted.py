# Given an array, check whether the array is in sorted order with recursion.

def isArraySorted(arr):
  if len(arr) == 1:
    return True
  return arr[0] <= arr[1] and isArraySorted(arr[1:])
