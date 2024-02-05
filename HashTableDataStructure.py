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
                # Update value if key already exists
                self.values[index] = value
                return
            index = self._linear_probe(index)

        # Key not found, insert new key-value pair
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self._find_key_index(key)
        if index is not None:
            return self.values[index]
        else:
            raise KeyError(f"Key not found: {key}")

    def peek(self, key):
        index = self._find_key_index(key)
        if index is not None:
            return self.values[index]
        else:
            return None

    def remove(self, key):
        index = self._find_key_index(key)
        if index is not None:
            self.keys[index] = None
            self.values[index] = None
        else:
            raise KeyError(f"Key not found: {key}")

    def size(self):
        return sum(1 for key in self.keys if key is not None)

    def is_empty(self):
        return self.size() == 0

    def _find_key_index(self, key):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return index
            index = self._linear_probe(index)

        return None


hash_table = MyHashTable(5)

#Inserting key-value pairs into the hash table
hash_table.put("apple", 5)
hash_table.put("guava", 6)
hash_table.put("banana", 8)
hash_table.put("orange", 12)

#Returns the current number of key-value pairs in the hash table.
print("Hash table size:", hash_table.size())
print("Is hash table empty?", hash_table.is_empty())

#Retrieves the value associated with a given key.
print("Value for key 'banana':", hash_table.get("banana"))
print("Value for key 'orange':", hash_table.get("orange"))

#Removes the key-value pair associated with the given key.
hash_table.remove("apple")

#Returns the hash table size after removal
print("Hash table size after removal:", hash_table.size())
print("Is hash table empty?", hash_table.is_empty())
