# Given a list containing numbers and nested list of numbers, calculate the sum of nested lists.

# lst = [1, 1, 1, [3, 4, [8]], [5]] => 23

# Recursive Solution
def nested_recursive_sum(lst):
    all_values_sum = 0
    for i in range(len(lst)):
        if type(lst[i]) == list:
            all_values_sum += nested_recursive_sum(lst[i])
        else:
            all_values_sum += lst[i]
    return all_values_sum


lst = [1, 1, 1, [3, 4, [8]], [5]]
print(nested_recursive_sum(lst))
