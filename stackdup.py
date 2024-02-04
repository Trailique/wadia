class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack underflow: cannot pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


# Testing the MyStack class
if __name__ == "__main__":
    stack = MyStack()

    # Test operations on an empty stack
    print("Is empty?", stack.is_empty())  # True
    # print(stack.pop())  # Should raise an exception
    # print(stack.peek())  # Should return None

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Is empty?", stack.is_empty())  # False
    print("Size:", stack.size())  # 3
    print("Peek:", stack.peek())  # 3

    print("Popping elements:")
    while not stack.is_empty():
        print(stack.pop())

    print("Is empty?", stack.is_empty())  # True
