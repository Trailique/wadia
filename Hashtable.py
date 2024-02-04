class MyHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def _rehash(self, old_hash):
        return (old_hash + 1) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        initial_index = index

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return

            index = self._rehash(index)
            if index == initial_index:
                raise Exception("Hash table is full.")

        self.keys[index] = key
        self.values[index] = value
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        initial_index = index

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = self._rehash(index)
            if index == initial_index:
                break

        raise KeyError("Key not found")

    def peek(self, key):
        index = self._hash(key)
        initial_index = index

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = self._rehash(index)
            if index == in
