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


my_array = MyArray(10)
print("Firstly,is the array empty?", my_array.is_empty())

#Appending array elements
my_array.append(11)
my_array.append(12)
my_array.append(13)
my_array.append(14)
my_array.append(15)
my_array.append(16)

#Printing the size of the array and the elements present
print("Array Elements:", [my_array.get(i) for i in range(my_array.size())])
print("Array size:", my_array.size())

#Set element 8 at index 1
my_array.set(1, 8)
print("Array after setting at index 1:", [my_array.get(i) for i in range(my_array.size())])

#Returning the peek element
last_element = my_array.peek()
print("Peek at the last element:", last_element)
print("Now,is the array empty?", my_array.is_empty())