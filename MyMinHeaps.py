class MyMinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def extract_min(self):
        if self.is_empty():
            raise IndexError("Heap underflow: The heap is empty")
        min_item = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self._heapify_down(0)
        return min_item

    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index
            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

# Example Usage
min_heap = MyMinHeap()
min_heap.insert(4)
min_heap.insert(2)
min_heap.insert(7)
min_heap.insert(1)

print("Peek min item:", min_heap.peek())  # Output: 1
print("Size of the min heap:", min_heap.size())  # Output: 4

print("Extract min item:", min_heap.extract_min())  # Output: 1
print("Size of the min heap after extraction:", min_heap.size())  # Output: 3
