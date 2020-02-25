# Given a string, calculate the length of the string
# Solve using both an iterative and recursive solution.

str_1 = "FiniteImpulseResponse"

# Iterative Solution
def string_length_iterative(str):
    count = 0
    for i in range(len(str)):
        count += 1
    return count

# Recursive Solution
def string_length_recursive(str):
    # Base Case
    if str == "":
        return 0
    # Recursive Case
    return 1 + string_length_recursive(str[1:])

print(string_length_recursive(str_1))
