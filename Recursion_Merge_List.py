# Merge two sorted list using recursion


# Recursive
def merge_list(lst1, lst2):
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    if lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    return [lst2[0]] + merge(lst1, lst2[1:])

# iterative
def merge_list(lst1, lst2):
    merge_list_length = len(lst1) + len(lst2)
    merge_list = [None] * merge_list_length

    idx_lst1 = 0
    idx_lst2 = 0
    idx_merge = 0

    while idx_merge < merge_list_length:
        lst1_exhausted = idx_lst1 >= len(lst1)
        lst2_exhausted = idx_lst2 >= len(lst2)
        if not lst1_exhausted and (lst2_exhausted or lst1[idx_lst1] < lst2[idx_lst2]):
            merge_list[idx_merge] = lst1[idx_lst1]
            idx_lst1 += 1
        else:
            merge_list[idx_merge] = lst2[idx_lst2]
            idx_lst2 += 1
        idx_merge += 1
    return merge_list

# Test
a = [1, 3, 5, 8, 9]
b = [2, 4, 6, 7, 9, 10]

print(merge_list(a, b))
