class MyHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.keys = [None] * capacity
        self.values = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def _linear_probe(self, index):
        return (index + 1) % self.capacity

    def put(self, key, value):
        hash_value = self._hash(key)
        index = hash_value

        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Update value if key already exists
                self.values[index] = value
                return
            index = self._linear_probe(index)

        # Key not found, insert new key-value pair
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        hash_value = self._hash(key)
        index = hash_value

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = self._linear_probe(index)

        # Key not found
        raise KeyError(f"Key '{key}' not found in the hash table")

    def peek(self, key):
        hash_value = self._hash(key)
        index = hash_value

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = self._linear_probe(index)

        # Key not found
        raise KeyError(f"Key '{key}' not found in the hash table")

    def remove(self, key):
        hash_value = self._hash(key)
        index = hash_value

        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Remove key-value pair
                self.keys[index] = None
                self.values[index] = None
                return
            index = self._linear_probe(index)

        # Key not found
        raise KeyError(f"Key '{key}' not found in the hash table")

    def size(self):
        return sum(1 for key in self.keys if key is not None)

    def is_empty(self):
        return self.size() == 0


hash_table = MyHashTable(capacity=10)
hash_table.put("a", 1)
hash_table.put("b", 2)
hash_table.put("c", 3)

print("Hash Table:")
for i in range(hash_table.capacity):
    if hash_table.keys[i] is not None:
        print(f"  {hash_table.keys[i]}: {hash_table.values[i]}")

print("Size:", hash_table.size())
print("Is empty:", hash_table.is_empty())

print("Get 'b':", hash_table.get("b"))
print("Peek 'c':", hash_table.peek("c"))

hash_table.remove("a")
print("After removing 'a':")
for i in range(hash_table.capacity):
    if hash_table.keys[i] is not None:
        print(f"  {hash_table.keys[i]}: {hash_table.values[i]}")
