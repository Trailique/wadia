class MyArray:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self.capacity = capacity
        self.data = [None] * capacity
        self.current_size = 0

    def get(self, index):
        if 0 <= index < self.current_size:
            return self.data[index]
        else:
            raise IndexError("Index out of bounds")

    def set(self, index, value):
        if 0 <= index < self.current_size:
            self.data[index] = value
        else:
            raise IndexError("Index out of bounds")

    def peek(self):
        if self.current_size > 0:
            return self.data[self.current_size - 1]
        else:
            raise IndexError("Array is empty")

    def size(self):
        return self.current_size

    def is_empty(self):
        return self.current_size == 0

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.current_size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append(self, value):
        if self.current_size == self.capacity:

            self.resize(2 * self.capacity)

        self.data[self.current_size] = value
        self.current_size += 1

my_array = MyArray(3)
my_array.append(1)
my_array.append(2)
my_array.append(3)
print("Size:", my_array.size())
print("Elements:", [my_array.get(i) for i in range(my_array.size())])
print("Element at index 1:", my_array.get(1))
my_array.set(1, 10)
print("Modified element at index 1:", my_array.get(1))
print("Peek:", my_array.peek())
print("Is empty:", my_array.is_empty())