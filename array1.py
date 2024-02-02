class MyArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def get(self, index):
        if not (0 <= index < self.size):
            raise IndexError("Index out of bounds")
        return self.array[index]

    def set(self, index, value):
        if not (0 <= index < self.size):
            raise IndexError("Index out of bounds")
        self.array[index] = value

    def peek(self):
        if self.is_empty():
            raise ValueError("Cannot peek from an empty array")
        return self.array[self.size - 1]

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def add(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = value
        self.size += 1


my_array = MyArray(3)
my_array.add(1)
my_array.add(2)
my_array.add(3)

print("Array:", my_array.array)
print("Size:", my_array.size)
print("Is empty:", my_array.is_empty())
print("Peek:", my_array.peek())

my_array.set(1, 5)
print("After setting index 1 to 5:", my_array.array)
print("Size:", my_array.size)
