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
