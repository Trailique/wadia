class DynamicArray:
    def __init__(self, initial_capacity):
        self.capacity = initial_capacity
        self.data = [None] * initial_capacity
        self.size = 0

    def get_element(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Index out of bounds")

    def get_array(self):
        return self.data

    def set_element(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of bounds")

    def peek_last(self):
        if self.size > 0:
            return self.data[self.size - 1]
        else:
            raise IndexError("Array is empty")

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def resize_array(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append_element(self, value):
        if self.size == self.capacity:
            self.resize_array(2 * self.capacity)
        self.data[self.size] = value
        self.size += 1


my_dynamic_array = DynamicArray(4)
my_dynamic_array.append_element(1)
my_dynamic_array.append_element(2)
my_dynamic_array.append_element(3)
my_dynamic_array.append_element(4)
my_dynamic_array.append_element(5)

print("Array:", my_dynamic_array.get_array())
print("Element at index 1:", my_dynamic_array.get_element(1))
my_dynamic_array.set_element(1, 10)
print("Updated element at index 1:", my_dynamic_array.get_element(1))
print("Last element:", my_dynamic_array.peek_last())
print("Size of the array:", my_dynamic_array.get_size())
print("Is the array empty?", my_dynamic_array.is_empty())