class MyArray:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._array = [None] * capacity

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def get(self, index):
        if 0 <= index < self._size:
            return self._array[index]
        else:
            raise IndexError("Index out of bounds")

    def set(self, index, value):
        if 0 <= index < self._size:
            self._array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def size(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def append(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)  # Double the capacity when full
        self._array[self._size] = value
        self._size += 1

    def __str__(self):
        return str(self._array[:self._size])


# Example usage:
my_array = MyArray()
print("Size:", my_array.size())
print("Is Empty:", my_array.isempty())

# Appending elements
for i in range(15):
    my_array.append(i)

# Printing the array
print("Array:", my_array)

# Accessing elements
print("Element at index 3:", my_array.get(3))

# Updating an element
my_array.set(2, 99)
print("Updated array:", my_array)

# Checking size and emptiness
print("Size:", my_array.size())
print("Is Empty:", my_array.isempty())

