class MyArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.length = 0

    def get(self, index):
        if 0 <= index < self.length:
            return self.data[index]
        else:
            raise IndexError("Index out of bounds")

    def set(self, index, value):
        if 0 <= index < self.length:
            self.data[index] = value
        else:
            raise IndexError("Index out of bounds")

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
            self.resize(self.capacity * 2)
        self.data[self.length] = value
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise IndexError("Array is empty")
        popped_value = self.data[self.length - 1]
        self.length -= 1
        if self.length <= self.capacity // 4:
            self.resize(self.capacity // 2)
        return popped_value


# Initialize with capacity 10
my_array = MyArray(10)

# Append elements
my_array.append(11)
my_array.append(12)
my_array.append(13)
my_array.append(14)
my_array.append(15)
my_array.append(16)

# Print size and elements
print("Size:", my_array.size())
print("Elements:", [my_array.get(i) for i in range(my_array.size())])

# Set element at index 1 to 2
my_array.set(1, 2)

# Print size and elements
print("Size:", my_array.size())
print("Elements:", [my_array.get(i) for i in range(my_array.size())])

# Print last element (peek)
print("Last Element:", my_array.peek())

# Pop an element
popped_value = my_array.pop()
print("Element popped:", popped_value)

# Print size and elements after popping
print("Size:", my_array.size())
print("Elements:", [my_array.get(i) for i in range(my_array.size())])
