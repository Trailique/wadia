class MyHashTable:
    def __init__(self, initial_capacity=10, load_factor=0.7):
        self.capacity = initial_capacity
        self.size = 0
        self.load_factor = load_factor
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def _linear_probe(self, index):
        return (index + 1) % self.capacity

    def _rehash(self):
        new_capacity = self.capacity * 2
        new_keys = [None] * new_capacity
        new_values = [None] * new_capacity
        for i in range(self.capacity):
            if self.keys[i] is not None:
                new_index = self._hash(self.keys[i])
                while new_keys[new_index] is not None:
                    new_index = self._linear_probe(new_index)
                new_keys[new_index] = self.keys[i]
                new_values[new_index] = self.values[i]
        self.capacity = new_capacity
        self.keys = new_keys
        self.values = new_values

    def put(self, key, value):
        if self.size / self.capacity >= self.load_factor:
            self._rehash()
        index = self._hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Update value for existing key
                self.values[index] = value
                return
            index = self._linear_probe(index)
        self.keys[index] = key
        self.values[index] = value
        self.size += 1

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
                self.size -= 1
                return
            index = self._linear_probe(index)

    def is_empty(self):
        return self.size == 0
