# Quicksort - simple implementation

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    print(f'pivot : {pivot}')
    left = [x for x in arr if x < pivot]
    print(left)
    middle = [x for x in arr if x == pivot]
    print(middle)
    right = [x for x in arr if x > pivot]
    print(right)
    return quicksort(left) + middle + quicksort(right)

# Test
arr = [ 7, 3, 8, 1, 6, 0, 9, 4, 5]

print(arr)
arr = quicksort(arr)
print(arr)
