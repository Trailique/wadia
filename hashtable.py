class MyHashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * capacity
        self.values = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def _probe(self, index):
        return (index + 1) % self.capacity

    def put(self, key, value):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = self._probe(index)

        self.keys[index] = key
        self.values[index] = value
        self.size += 1

 
        if self.size > self.capacity * 0.7:
            self._resize()

    def get(self, key):
        index = self._find_key_index(key)
        return self.values[index] if index is not None else None

    def peek(self, key):
        index = self._find_key_index(key)
        return self.values[index] if index is not None else None

    def remove(self, key):
        index = self._find_key_index(key)
        if index is not None:
            self.keys[index] = None
            self.values[index] = None
            self.size -= 1

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _find_key_index(self, key):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return index
            index = self._probe(index)

        return None

    def _resize(self):
        new_capacity = self.capacity * 2
        new_keys = [None] * new_capacity
        new_values = [None] * new_capacity

        for i in range(self.capacity):
            if self.keys[i] is not None:
                new_index = self._hash(self.keys[i])

                while new_keys[new_index] is not None:
                    new_index = self._probe(new_index)

                new_keys[new_index] = self.keys[i]
                new_values[new_index] = self.values[i]

        self.keys = new_keys
        self.values = new_values
        self.capacity = new_capacity




hash_table = MyHashTable(5)


hash_table.put("apple", 5)
hash_table.put("banana", 8)
hash_table.put("cherry", 12)
hash_table.put("date", 3)


print("Value for 'apple':", hash_table.get("apple"))
print("Value for 'banana':", hash_table.get("banana"))
print("Value for 'cherry':", hash_table.get("cherry"))


print("Size of hash table:", hash_table.get_size())
print("Is the hash table empty?", hash_table.is_empty())


hash_table.remove("banana")
print("Size after removing 'banana':", hash_table.get_size())


print("Peek at the value for 'date':", hash_table.peek("date"))


print("Value for 'grape':", hash_table.get("grape"))
