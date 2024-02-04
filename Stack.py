class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

stack = MyStack()

print("Checking ......",stack.is_empty())  

stack.push(1)
stack.push(2)
stack.push(3)

print("Element from top of Stack is",stack.peek()) 

print("Removed elements are",stack.pop()) 
print("Removed elements are",stack.pop()) 

print("After Action Size of Stack",stack.size()) 

print("Checking ......",stack.is_empty()) 
