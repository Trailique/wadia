class MyStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

# Example usage:
stack = MyStack()

print("Is stack empty?", stack.is_empty())  

stack.push(1)
stack.push(2)
stack.push(3)

print("Top of the stack:", stack.peek()) 
print("Size of the stack:", stack.size()) 
popped_item = stack.pop()
stack.pop()
print("Top of the stack:", stack.peek()) 
print("Popped item:", popped_item)
stack.pop()

print("Is stack empty?", stack.is_empty())  
print("Size of the stack:", stack.size())  
