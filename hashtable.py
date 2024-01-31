class MyHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * capacity
        self.values = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def _probe(self, index):
        return (index + 1) % self.capacity

    def _find_index(self, key):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return index
            index = self._probe(index)

        return None

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

    def get(self, key):
        index = self._find_index(key)
        if index is not None:
            return self.values[index]
        raise KeyError(key)

    def peek(self, key):
        index = self._find_index(key)
        if index is not None:
            return self.values[index]
        return None

    def remove(self, key):
        index = self._find_index(key)
        if index is not None:
            self.keys[index] = None
            self.values[index] = None
            self.size -= 1
        else:
            raise KeyError(key)

    def get_size(self):  # Rename the method to avoid conflicts
        return self.size

    def is_empty(self):
        return self.size == 0

# Example usage:
if __name__ == '__main__':
    ht = MyHashTable(5)

    ht.put("apple", 3)
    ht.put("banana", 2)
    ht.put("cherry", 5)

    print("Size:", ht.get_size())  # Output: 3
    print("Is Empty:", ht.is_empty())  # Output: False

    print("Get banana:", ht.get("banana"))  # Output: 2
    print("Peek durian:", ht.peek("durian"))  # Output: None

    ht.put("banana", 4)
    print("Updated value for banana:", ht.get("banana"))  # Output: 4

    ht.remove("apple")
    print("Size after removal:", ht.get_size())  # Output: 2
