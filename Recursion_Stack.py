# Write a recursive function that insert an element at the bottom of a stack.

class Stack(object):
    def __init__(self):
        self.stack = list()
        self.size = 0

    def add(self, value):
        self.stack.insert(0, value)
        self.size += 1

    def remove(self):
        if self.size > 0:
            self.size -= 1
        return self.stack.pop(0)

    def view(self):
        print(self.stack)


# Insert at bottom Iterative
def addAtBottomIterative(stack, value):
    secondary = Stack()
    while stack.size != 0:
        secondary.add(stack.remove())
    stack.add(value)
    while secondary.size != 0:
        stack.add(secondary.remove())


# Insert at bottom Recursive
def addAtBottomRecursive(stack, value):
    # Base case
    if stack.size == 0:
        stack.add(value)
        return
    # Recursive case
    top = stack.remove()
    addAtBottomRecursive(stack, value)
    stack.add(top)


# Test
st = Stack()
for i in range(6):
    st.add(i)

st.view()
addAtBottomIterative(st, -1)
addAtBottomRecursive(st, -2)
st.view()
