class MyStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack underflow: cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError("Cannot peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)
print("Size:", stack.size())
print("Peek:", stack.peek())

popped_item = stack.pop()
print("Popped:", popped_item)
print("Stack after pop:", stack.items)
print("Is empty:", stack.is_empty())
