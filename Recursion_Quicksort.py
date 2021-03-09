# Quicksort - simple implementation

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# Verbose Quicksort, help to understand recursive quicksort
def quicksort_verbose(arr):
    if len(arr) <= 1:
        print(f'Base case return {arr}')
        return arr
    # Choosing a pivot
    pivot = arr[len(arr) // 2]
    print((f'Choosing a new pivot : {pivot}'))

    # Move value to the left according to pivot
    left = [x for x in arr if x < pivot]
    print(f'Left : {left}')

    middle = [x for x in arr if x == pivot]
    print(f'Middle : {middle}')

    # Move value to the right according to pivot
    right = [x for x in arr if x > pivot]
    print(f'Right : {right}')

    to_return = quicksort_verbose(left) + middle + quicksort_verbose(right)
    print(f'Returning {to_return}')

    return to_return

# Test
arr = [ 7, 3, 8, 1, 6, 0, 9, 4, 5]

print(arr)
arr = quicksort_verbose(arr)
print(arr)
