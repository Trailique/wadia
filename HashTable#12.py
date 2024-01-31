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
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = self._linear_probe(index)

        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = self._linear_probe(index)

        raise KeyError(f"Key not found: {key}")

    def peek(self, key):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = self._linear_probe(index)

        raise KeyError(f"Key not found: {key}")

    def remove(self, key):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                return
            index = self._linear_probe(index)

        raise KeyError(f"Key not found: {key}")

    def size(self):
        return sum(1 for key in self.keys if key is not None)

    def is_empty(self):
        return self.size() == 0


hash_table = MyHashTable(5)
hash_table.put("key1", "value1")
hash_table.put("key2", "value2")
hash_table.put("key3", "value3")

print("Hash table size:", hash_table.size())  
print("Value for key 'key2':", hash_table.get("key2"))  

hash_table.remove("key1")
print("Updated hash table size:", hash_table.size())  
print("Is hash table empty?", hash_table.is_empty())  