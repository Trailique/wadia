class MyMinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up()

    def extract_min(self):
        if self.is_empty():
            raise IndexError("Heap underflow: Trying to extract from an empty heap")
        
        self._swap(0, len(self.heap) - 1)
        min_item = self.heap.pop()
        self._heapify_down()
        return min_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _heapify_down(self):
        index = 0
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

print("Min heap after insertion:", min_heap.heap)

print("Min element:", min_heap.peek())

print("Extracted min element:", min_heap.extract_min())
print("Min heap after extraction:", min_heap.heap)

print("Is the heap empty?", min_heap.is_empty())
print("Current size of the heap:", min_heap.size())
