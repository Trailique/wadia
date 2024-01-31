
class MyArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.length = 0

    def resize(self, new_capacity):
        new_arr = [None] * new_capacity
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.capacity = new_capacity
        self.arr = new_arr

    def get(self, index):
        if 0 <= index < self.length:
            return self.arr[index]
        else:
            raise IndexError("Value is out of range")

    def set(self, index, value):
        if 0 <= index < self.length:
            self.arr[index] = value
        else:
            raise IndexError("Value is out of range")

    def peek(self):
        if self.is_empty():
            raise Exception("Array is empty Cannot peek into an empty array")
        return self.arr[self.length - 1]

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def append(self, value):
        if self.length == self.capacity:
            self.resize(2 * self.capacity)

        self.arr[self.length] = value
        self.length += 1

my_array = MyArray(5)
print("Is the array empty", my_array.is_empty()) 

my_array.append(1)
my_array.append(2)
my_array.append(3)
print("Array size:", my_array.size()) 
my_array.set(1, 10)
print("Element at index 1:", my_array.get(1))  

print("Last element (peek):", my_array.peek()) 

my_array.append(4)
my_array.append(5)
print("Array size after appending:", my_array.size())