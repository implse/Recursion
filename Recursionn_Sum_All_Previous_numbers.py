# Given a list of integers, write a recursive function that add sum of all the previous
# numbers to each index of the list.


# Recursive Solution : Top to Bottom (Head recursionn)
def sum_recursive(lst, idx):
    if idx <= 1:
        return
    sum_recursive(lst, idx - 1)
    lst[idx - 1] += lst[idx - 2]


lst = [1, 2, 3, 4, 5, 6]
sum_recursive(lst, len(lst))
print(lst)


# Recursive Solution : Bottom Up
def sum_recursive(lst, idx, len, sum = 0):
    if idx == len:
        return
    lst[idx] = lst[idx] + sum
    sum_recursive(lst, idx + 1, len, lst[idx])


lst = [1, 2, 3, 4, 5, 6]
sum_recursive(lst, 0, len(lst), 0)
print(lst)

# Iterative Solution
def sum_iterative(lst):
    for i in range(1, len(lst)):
        lst[i] += lst[i - 1]
    return lst


lst = [1, 2, 3, 4, 5, 6]
sum_iterative(lst)
print(lst)
