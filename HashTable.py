class MyHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def hash_function(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value  # Update value for existing key
                return
            index = (index + 1) % self.capacity  # Linear probing
        self.keys[index] = key
        self.values[index] = value
        self.size += 1

    def get(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.capacity  # Linear probing
        raise KeyError("Key not found")

    def peek(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.capacity  # Linear probing
        raise KeyError("Key not found")

    def remove(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.size -= 1
                return
            index = (index + 1) % self.capacity  # Linear probing
        raise KeyError("Key not found")

    def get_size(self):  # Renamed method to avoid conflict with attribute
        return self.size

    def is_empty(self):
        return self.size == 0

# Example usage:
hash_table = MyHashTable(10)
hash_table.put("a", 1)
hash_table.put("b", 2)
hash_table.put("c", 3)

print(hash_table.get("b"))  # Output: 2
print(hash_table.peek("c"))  # Output: 3

hash_table.remove("b")
print(hash_table.get_size())  # Output: 2
print(hash_table.is_empty())  # Output: False
