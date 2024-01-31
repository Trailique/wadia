class MyArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.length = 0

    def get(self, index):
        if 0 <= index < self.length:
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def set(self, index, value):
        if 0 <= index < self.length:
            self.data[index] = value
        else:
            raise IndexError("Index out of range")

    def peek(self):
        if self.length > 0:
            return self.data[self.length - 1]
        else:
            raise IndexError("Array is empty")

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append(self, value):
        if self.length == self.capacity:
            self.resize(2 * self.capacity)
        self.data[self.length] = value
        self.length += 1

# Example usage:
my_array = MyArray(5)
print("Initial array:")
print("Size:", my_array.size())
print("Is empty:", my_array.is_empty())

my_array.append(1)
my_array.append(2)
my_array.append(3)
my_array.append(4)
my_array.append(5)

print("\nArray after adding elements:")
print("Size:", my_array.size())
print("Is empty:", my_array.is_empty())

print("Element at index 2:", my_array.get(2))
print("Last element:", my_array.peek())

my_array.set(2, 10)
print("Updated element at index 2:", my_array.get(2))

# Resize test
my_array.append(6)
print("\nArray after resizing:")
print("Size:", my_array.size())
print("Is empty:", my_array.is_empty())
print("New capacity:", my_array.capacity)
