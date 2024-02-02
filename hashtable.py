class MyHashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.keys = [None] * capacity
        self.values = [None] * capacity

    def _hash_function(self, key):
        return hash(key) % self.capacity

    def _linear_probe(self, index):
        return (index + 1) % self.capacity

    def put(self, key, value):
        index = self._hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:

                self.values[index] = value
                return

            index = self._linear_probe(index)

        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self._hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = self._linear_probe(index)

        return None

    def peek(self, key):
        index = self._hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = self._linear_probe(index)

        return None

    def remove(self, key):
        index = self._hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:

                self.keys[index] = None
                self.values[index] = None
                return

            index = self._linear_probe(index)

    def size(self):
        return sum(1 for key in self.keys if key is not None)

    def is_empty(self):
        return self.size() == 0


hash_table = MyHashTable()

hash_table.put("one", 1)
hash_table.put("two", 2)
hash_table.put("three", 3)

print("Current Hash Table:")
for key, value in zip(hash_table.keys, hash_table.values):
    if key is not None:
        print(f"{key}: {value}")

print("Get value for 'two':", hash_table.get("two"))
print("Peek value for 'three':", hash_table.peek("three"))

hash_table.remove("two")

print("Size:", hash_table.size())
print("Is Empty:", hash_table.is_empty())
