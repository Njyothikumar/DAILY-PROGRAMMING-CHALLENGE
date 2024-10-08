class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __repr__(self):
        return repr(self.items)


def insert_at_bottom(stack, element):
    """ Helper function to insert an element at the bottom of the stack. """
    if stack.is_empty():
        stack.push(element)
    else:
        top = stack.pop()
        insert_at_bottom(stack, element)
        stack.push(top)


def reverse_stack(stack):
    """ Function to reverse the stack using recursion. """
    if not stack.is_empty():
        top = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, top)


s = Stack()
for num in [1, 2, 3, 4]:
    s.push(num)

print("Original stack:", s)
reverse_stack(s)
print("Reversed stack:", s)
