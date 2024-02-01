class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            print("Error: Stack underflow. Cannot pop from an empty stack.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Error: Cannot peek from an empty stack.")
            return None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

stack = MyStack()

for i in range(1, 10):
    stack.push(i)

#Printing the stack elements and stack size
print("Stack:", stack.stack)
print("Stack Size:", stack.size())
print("Is stack empty?", stack.is_empty())

#Returning the element from the top of the stack
print("Peek at the top element:", stack.peek())

for i in range(5):
    popped_item = stack.pop()
    print("Popped item:", popped_item)

#Popping the elements
print("Stack after popping elements:", stack.pop())
print("Stack Size after pop:", stack.size())
print("Is stack empty?", stack.is_empty())
