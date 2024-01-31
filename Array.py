class MyArray:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._array = [None] * capacity

    def get(self, index):
        if 0 <= index < self._size:
            return self._array[index]
        else:
            raise IndexError("Index out of range")

    def set(self, index, value):
        if 0 <= index < self._size:
            self._array[index] = value
        else:
            raise IndexError("Index out of range")

    def peek(self):
        if self._size > 0:
            return self._array[self._size - 1]
        else:
            raise IndexError("Array is empty")

    @property
    def size(self):
        return self._size

    @property
    def is_empty(self):
        return self._size == 0

    def append(self, value):
        if self._size == self._capacity:
            self._resize()
        self._array[self._size] = value
        self._size += 1

    def _resize(self):
        self._capacity *= 2
        new_array = [None] * self._capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array

    def display(self):
        print(self._array[:self._size])

# Example usage:
my_array = MyArray()

# Append values
for i in range(10):
    my_array.append(i)

# Display the array
my_array.display()

# Access elements
print("Element at index 3:", my_array.get(3))

# Modify an element
my_array.set(2, 100)

# Display the modified array
my_array.display()

# Peek at the last element
print("Last element:", my_array.peek())

# Get the size of the array
print("Size of the array:", my_array.size)

# Check if the array is empty
print("Is the array empty?", my_array.is_empty)
