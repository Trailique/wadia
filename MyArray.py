class MyArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.length = 0

    def get(self, index):
        if 0 <= index < self.length:
            return self.data[index]
        else:
            return None

    def set(self, index, value):
        if 0 <= index < self.length:
            self.data[index] = value

    def peek(self):
        if self.length > 0:
            return self.data[self.length - 1]
        else:
            return None

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def resize(self, new_capacity):
        if new_capacity > self.capacity:
            self.data.extend([None] * (new_capacity - self.capacity))
            self.capacity = new_capacity

    def append(self, value):
        if self.length == self.capacity:
            self.resize(2 * self.capacity)
        self.data[self.length] = value
        self.length += 1

# Create an instance of MyArray
my_array = MyArray(3)
my_array.append(1)
my_array.append(2)
my_array.append(3)
my_array.append(4)
my_array.append(5)

print("Array:", my_array.data)
print("Element at index 1:", my_array.get(1))
my_array.set(1, 10)
print("Updated element at index 1:", my_array.get(1))
print("Last element:", my_array.peek())
print("Size of the array:", my_array.size())
print("Is the array empty?", my_array.is_empty())
