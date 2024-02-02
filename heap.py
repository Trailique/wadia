class MyMinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if self.is_empty():
            raise ValueError("Heap underflow: cannot extract from an empty heap")

        # Swap the root (min element) with the last element
        self._swap(0, len(self.heap) - 1)
        min_value = self.heap.pop()

        # Restore heap property by heapifying down
        if len(self.heap) > 0:
            self._heapify_down(0)

        return min_value

    def peek(self):
        if self.is_empty():
            raise ValueError("Cannot peek from an empty heap")
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

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
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

min_heap = MyMinHeap()
min_heap.insert(4)
min_heap.insert(2)
min_heap.insert(7)
min_heap.insert(1)

print("Min Heap:", min_heap.heap)
print("Size:", min_heap.size())
print("Is empty:", min_heap.is_empty())
print("Peek:", min_heap.peek())

min_value = min_heap.extract_min()
print("Extracted Min:", min_value)
print("Min Heap after extraction:", min_heap.heap)
