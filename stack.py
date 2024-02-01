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
            raise IndexError("peek from an empty stack")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Size:", stack.size())  
print("Peek:", stack.peek())  
print("Pop:", stack.pop())    
print("Is Empty:", stack.is_empty())  
