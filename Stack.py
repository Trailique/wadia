class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


# Example usage:
my_stack = MyStack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Top of the stack:", my_stack.peek())
print("Stack size:", my_stack.size())

popped_item = my_stack.pop()
print("Popped item:", popped_item)
print("Stack size after pop:", my_stack.size())
print("Is the stack empty?", my_stack.is_empty())

# Try to pop from an empty stack (edge case)
empty_stack = MyStack()
# The next line would raise an IndexError: empty_stack.pop()
