class MyStack:
    def __init__(self):
        self.arr = []

    def push(self, item):
        self.arr.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop as the stack is empty")
        return self.arr.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Cannot peek as the stack is empty")
        return self.arr[-1]

    def size(self):
        return len(self.arr)

    def is_empty(self):
        return len(self.arr) == 0


stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())  
print("Top of the stack:", stack.peek())  

popped_item = stack.pop()
print("Popped item:", popped_item)  
print("Updated stack size:", stack.size())  
print("Is stack empty?", stack.is_empty())  


try:
    empty_stack_pop = stack.pop()
except Exception as e:
    print(f"Exception: {e}")  

