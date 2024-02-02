class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:

            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack = []


stack = MyStack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Current Stack:", stack.stack)
print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Size:", stack.size())
print("Is Empty:", stack.is_empty())


stack.clear()

print("After Clearing:")
print("Current Stack:", stack.stack)
print("Is Empty:", stack.is_empty())
