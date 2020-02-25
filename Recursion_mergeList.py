# Merge two sorted list using recursion

def merge(lst1, lst2):
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    if lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    return [lst2[0]] + merge(lst1, lst2[1:])
