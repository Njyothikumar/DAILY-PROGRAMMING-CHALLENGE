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


def sorted_insert(stack, element):
    """ Helper function to insert an element into the sorted stack. """
    if stack.is_empty() or element > stack.peek():
        stack.push(element)
    else:
        top = stack.pop()
        sorted_insert(stack, element)
        stack.push(top)


def sort_stack(stack):
    """ Function to sort the stack. """
    if not stack.is_empty():
        top = stack.pop()
        sort_stack(stack)
        sorted_insert(stack, top)
s = Stack()
for num in [3, 1, 4, 2]:
    s.push(num)

print("Original stack:", s)
sort_stack(s)
print("Sorted stack:", s)
