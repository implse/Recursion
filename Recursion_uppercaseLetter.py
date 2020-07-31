# Given a string, find the first uppercase character.
# Solve using both an iterative and recursive solution.

str_1 = "finiteImpulse"
str_2 = "FiniteImpulse"
str_3 = "finiteimpulse"


# Iterative
def findUpper_iterativre(str):
    for i in range(len(str)):
        if str[i].isupper():
            return (str[i], i)
    return "No uppercase character found"


# Recursive
def findUpper_recursive(str, index=0):
    # Condition Case
    if str[index].isupper():
        return (str[index], index)
    # Base Case
    if index == len(str) - 1:
        return "No uppercase character found"
    # Recursive case
    return findUpper_recursive(str, index + 1)


print(findUpper_recursive(str_1, 0))
print(findUpper_recursive(str_2, 0))
print(findUpper_recursive(str_3, 0))
