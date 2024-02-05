class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek from an empty stack")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

# Example usage:
stack = MyStack()
print(stack.is_empty())  # True

stack.push(5)
stack.push(10)
stack.push(15)

print(stack.size())  # 3
print(stack.peek())  # 15

print(stack.pop())  # 15
print(stack.size())  # 2
print(stack.is_empty())  # False
