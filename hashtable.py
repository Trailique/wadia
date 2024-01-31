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
        return None

    def peek(self, key):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = self._linear_probe(index)

        return None

    def remove(self, key):
        index = self._hash(key)

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
my_hash_table = MyHashTable(5)
my_hash_table.put("a", 1)
my_hash_table.put("b", 2)
my_hash_table.put("c", 3)

print("Value for key 'b':", my_hash_table.get("b"))
my_hash_table.remove("b")
print("Check Whether Is empty:", my_hash_table.is_empty())
print("ACtual Size:", my_hash_table.size())
